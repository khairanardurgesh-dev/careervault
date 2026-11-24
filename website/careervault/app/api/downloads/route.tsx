import type { NextRequest } from "next/server";
import { NextResponse } from "next/server";
import { createServiceRoleClient } from "@/lib/supabase";

export async function GET(req: NextRequest) {
  try {
    const authHeader = req.headers.get("authorization");
    if (!authHeader) {
      return NextResponse.json({ message: "Unauthorized" }, { status: 401 });
    }

    const token = authHeader.replace("Bearer ", "");
    const supabase = createServiceRoleClient();

    const { data: { user }, error: authError } = await supabase.auth.getUser(token);
    if (authError || !user) {
      return NextResponse.json({ message: "Invalid session" }, { status: 401 });
    }

    // Get customer
    const { data: customer } = await supabase
      .from("customers")
      .select("*")
      .eq("auth_user_id", user.id)
      .single();

    if (!customer) {
      return NextResponse.json({ message: "Customer not found" }, { status: 404 });
    }

    // Get entitlements
    const { data: entitlements } = await supabase
      .from("entitlements")
      .select("*, products(*)")
      .eq("customer_id", customer.id)
      .eq("status", "active");

    if (!entitlements || entitlements.length === 0) {
      return NextResponse.json({ message: "No active entitlements" }, { status: 403 });
    }

    const { searchParams } = new URL(req.url);
    const assetId = searchParams.get("assetId");

    if (assetId) {
      // Verify asset belongs to entitled product
      const { data: asset } = await supabase
        .from("download_assets")
        .select("*")
        .eq("id", assetId)
        .eq("is_active", true)
        .single();

      if (!asset) {
        return NextResponse.json({ message: "Asset not found" }, { status: 404 });
      }

      const hasEntitlement = entitlements.some((e) => e.product_id === asset.product_id);
      if (!hasEntitlement) {
        return NextResponse.json({ message: "Not entitled" }, { status: 403 });
      }

      // Create signed URL (short-lived)
      const { data: signedUrl } = await supabase.storage
        .from("careervault-products")
        .createSignedUrl(asset.asset_path, 300); // 5 minutes

      // Log download event
      await supabase.from("download_events").insert({
        customer_id: customer.id,
        asset_id: asset.id,
        outcome: "success",
      });

      return NextResponse.json({ download_url: signedUrl?.signedUrl });
    }

    // List available assets
    const productIds = entitlements.map((e) => e.product_id);
    const { data: assets } = await supabase
      .from("download_assets")
      .select("*")
      .in("product_id", productIds)
      .eq("is_active", true);

    return NextResponse.json({ assets: assets || [] });
  } catch (error) {
    console.error("Downloads error:", error);
    return NextResponse.json({ message: "Internal server error" }, { status: 500 });
  }
}
