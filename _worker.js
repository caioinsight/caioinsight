// Cowy edge Worker — gates /internal/* behind HTTP Basic Auth, serves everything else as static assets.
// The password is NOT in this file. It lives as a Cloudflare secret: INTERNAL_PASSWORD.
// Set it once:  Workers & Pages > caioinsight > Settings > Variables and Secrets > Add secret
//   Name: INTERNAL_PASSWORD   Value: <the password>   (type: Secret)
// Username is "caioadmin" (usernames aren't secret, so it can live in code).

const USERNAME = "caioadmin";

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (url.pathname.startsWith("/internal/")) {
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

    // Authorized (or public path) — serve the static asset.
    return env.ASSETS.fetch(request);
  },
};
