# Cowy · Stripe Checkout Setup

Step-by-step to turn the intake form's upgrade buttons into real, working checkout. Budget about 10 minutes. This is the one part only you can do (your account, your bank, your identity).

---

## Phase 1 · One-time account setup

1. Go to **stripe.com** and create an account (or sign in).
2. Complete **activation**: business details + the bank account where payouts land. Stripe can't pay you until this is done. This step needs your real identity and banking, so it's unavoidably yours.
3. Stay in **Test mode** (toggle, top-right) while you build. Make the links, test them with card `4242 4242 4242 4242` (any future expiry, any CVC), then switch to **Live mode** and recreate them for real cards.
   - Note: test-mode and live-mode links are **different URLs**. You'll paste the live ones in when you're ready to charge real money.

---

## Phase 2 · Create the three Payment Links

In Stripe: **Product catalog → Payment links → + New** (or **Payments → Payment Links**). Make each of these.

### Link 1 — Full report
- Product name: `Cowy AI Visibility Report`
- Description: `One-time AI visibility audit. Credited toward your monthly plan if you continue within 30 days.`
- Price: **$1,500.00** · **One-time**
- Save → copy the `https://buy.stripe.com/...` link → this is your **report** link.

### Link 2 — AI Watchdog
- Product name: `Cowy AI Watchdog`
- Description: `Monthly monitoring. We alert you when AI states a wrong fact about your brand or a competitor overtakes you.`
- Price: **$79.00** · **Recurring → Monthly**
- Save → copy link → this is your **watchdog** link.

### Link 3 — Done For You
- Product name: `Cowy Done For You`
- Description: `Done-for-you AI visibility. Monthly fixes, a scoreboard, and proof of the lift.`
- Price: **$2,500.00** · **Recurring → Monthly**
- Save → copy link → this is your **dfy** link.

---

## Phase 3 · Settings to turn on (per link, under "Options")

- **Collect customer email** → ON. This is how you match a payment to the right lead in your tracker.
- **Allow promotion codes** → ON. This is how you apply the report credit (below).
- Subscriptions: leave free trial OFF unless you want one.

---

## Phase 4 · The "$1,500 credited toward the retainer" promise

Payment Links can't auto-credit one purchase against another, so do it with a coupon:

1. **Product catalog → Coupons → + New**: **$1,500 off**, duration **Once**, name it `REPORT-CREDIT`.
2. When a report client upgrades to Done For You, give them that code at the Done-For-You checkout.
3. Their first month becomes **$1,000** ($2,500 − $1,500) — exactly the credit you promised.
4. Because "Allow promotion codes" is ON, they can enter it themselves, or you send the link + code.

This keeps the promise real with no custom code.

---

## Phase 5 · Wire the links into the form

Send the three links and they get pasted into the form's `CHECKOUT` config:

```
report:   https://buy.stripe.com/...
watchdog: https://buy.stripe.com/...
dfy:      https://buy.stripe.com/...
```

Until they're filled in, each button gracefully says "Reply to your email and we will send you a secure checkout link," so it's never a dead button.

---

## Honest prerequisites before going LIVE

- The buttons only actually open Stripe from a **live URL** (your deployed site or a Netlify Drop link), not the raw file preview — browser sandbox blocks the pop-up otherwise. So the order is: create links → paste them in → deploy the page → buttons work end to end.
- Before flipping to **Live mode** and taking real money, have the basics in place:
  - A business entity or sole-proprietor setup.
  - Simple **Terms** and a **refund policy** on the site. You promise "credited back" and "no lift, you don't pay," so that needs to be written down. Taking payments without these is a risk.

---

## Quick reference: which link powers which button

| Form button | Stripe link slot | Price | Type |
|---|---|---|---|
| Get the full report | `report` | $1,500 | one-time |
| Add Watchdog | `watchdog` | $79 | monthly |
| Go Done For You | `dfy` | $2,500 | monthly |
