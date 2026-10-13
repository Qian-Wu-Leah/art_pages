# wu-qian.com — static site

Plain HTML/CSS/JS, no build step, no frameworks, no third-party trackers.
Pages: Home, Painting, CG, Statement, Resume, Contact.

## 1. Get the images (one time, on your own computer)

The artwork lives on Wix's servers. Before you cancel Wix, run:

    python3 download_images.py

This fills the `images/` folder (43 files). Open `index.html` in a browser to check it.
**Do this before cancelling Wix**, and keep your own backup of the original full-size artwork too.

## 2. Contact form (one time)

1. Sign up free at https://formspree.io and create a form for qwu0101@gmail.com.
2. Copy the form ID (the part after `/f/`).
3. In `contact.html`, replace `YOUR_FORM_ID` with it.

(Until you do this, the email and phone shown on the page still work.)

## 3. Deploy on Cloudflare Pages (recommended: free, fast, secure)

Cost: $0 hosting with unlimited bandwidth, free HTTPS, global CDN, DDoS protection.
You only pay for the domain name itself (about $10/yr at Cloudflare Registrar, at cost).

1. Create a free account at https://dash.cloudflare.com.
2. Workers & Pages -> Create -> Pages -> **Upload assets** (direct upload).
3. Name the project, drag in this whole folder (including `images/`), click Deploy.
4. Open the project -> Custom domains -> add `www.wu-qian.com` and `wu-qian.com`.
5. Domain: either move DNS to Cloudflare (it walks you through it) or add the CNAME record it shows at your current registrar.
   - Your domain is currently connected to Wix; disconnect it there first, and **keep the Wix plan until the new site is live** so there is no downtime.
   - If the domain was bought through Wix, you can transfer it out to Cloudflare Registrar or another registrar to stop paying Wix prices.

Alternatives (also free): Netlify (same drag-and-drop; `_headers` and `_redirects` work there), GitHub Pages, Vercel.

## Files

- `style.css`, `site.js` — styling, lightbox gallery, contact form handler
- `_headers` — security headers + caching (Cloudflare Pages / Netlify)
- `_redirects` — keeps old URLs like `/painting` working
- `download_images.py` — pulls the artwork from the Wix CDN
