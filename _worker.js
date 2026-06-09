// Cowy edge Worker — gates /internal/* behind HTTP Basic Auth, serves everything else as static assets.
// The password is NOT in this file. It lives as a Cloudflare secret: INTERNAL_PASSWORD.
// Set it once:  Workers & Pages > caioinsight > Settings > Variables and Secrets > Add secret
//   Name: INTERNAL_PASSWORD   Value: <the password>   (type: Secret)
// Username is "caioadmin" (usernames aren't secret, so it can live in code).

const USERNAME = "caioadmin";

// Internal/founder-only paths. Anything matching here requires Basic Auth.
function isGated(pathname) {
  return pathname.startsWith("/internal/")
    || pathname === "/dashboard.html"
    || pathname === "/glossary.html"
    || pathname === "/dashboard-data.json";
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (isGated(url.pathname)) {
      const pass = env.INTERNAL_PASSWORD;
      const expected = pass ? "Basic " + btoa(`${USERNAME}:${pass}`) : null;
      const provided = request.headers.get("Authorization") || "";

      if (!expected || provided !== expected) {
        return new Response("Authentication required.", {
          status: 401,
          headers: {
            "WWW-Authenticate": 'Basic realm="Cowy Internal", charset="UTF-8"',
            "Cache-Control": "no-store",
          },
        });
      }
    }

    // Serve the static asset; force gated/dynamic pages to always revalidate (no stale dashboard).
    const resp = await env.ASSETS.fetch(request);
    if (isGated(url.pathname)) {
      const r = new Response(resp.body, resp);
      r.headers.set("Cache-Control", "no-store, must-revalidate");
      return r;
    }
    return resp;
  },
};
