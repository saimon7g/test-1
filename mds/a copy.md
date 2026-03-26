# Digital Product Passport (DPP) — Portfolio Summary

## What it is

A **Digital Product Passport** platform for the **textile and apparel supply chain**, aligned with multi-tier traceability (farmer → spinner → dyer → manufacturer → brand). Companies register with role-specific profiles, manage **orders** (product spec, BOM, packaging, compliance requirements), **batches**, and **certificate linkage**; minted DPPs are exposed via **public, shareable links** with optional **verifier workflows** (password-protected verification links, approve/decline decisions).

## What I built / achieved

- **End-to-end domain model** for registration, contacts, certifications, audits, suppliers, purchase orders, orders, batches, and a denormalized **`DppRecord`** snapshot for public consumption.
- **REST API** (Next.js Route Handlers) with consistent `{ success, data | error }` responses, **Zod**-validated inputs, and **JWT Bearer** auth for private routes.
- **Public DPP surface**: resolve DPP by opaque token (and backward compatibility for legacy JWT-shaped tokens), serve **JSON-LD** product data and **Verifiable Credentials / Verifiable Presentations** signed with **Ed25519** (W3C-style proofs, RFC 8785 canonicalization for signing).
- **Cryptography & keys**: per-company **Ed25519** key pairs with **encrypted private key** storage; platform signing/verification helpers and **`.well-known`** style exposure for verification material.
- **Angular SPA**: lazy-loaded feature routes, **route guards** (guest, authenticated, company admin, super admin), company profile editing, order/batch flows, **QR** generation for DPP links, and **public** pages for DPP display and batch verification.

## Stack

| Layer | Technologies |
|--------|----------------|
| **Backend** | Next.js (App Router), TypeScript, React 19 (runtime for Next) |
| **Data** | PostgreSQL, Prisma ORM, migrations |
| **Auth** | JWT (middleware + `verifyToken`), NextAuth / Prisma adapter in dependencies |
| **Validation** | Zod |
| **Security** | bcrypt (passwords), encrypted company private keys, scoped public vs private API paths |
| **Frontend** | Angular 17 (standalone components), RxJS, Angular CDK |
| **UI** | Tailwind CSS, Flowbite, Lucide icons |
| **Interop** | `qrcode` for link/label use cases |

*Note: The repo may also include **Hyperledger Fabric** sample material under `dpp_blockchain/` for exploration; the described product path above is centered on **dppbackend** + **dppweb**.*

## Architecture & structure

- **Monorepo-style layout**: `dppbackend/` (API + data), `dppweb/` (Angular client), optional blockchain samples separate from the main app.
- **Backend**: `src/app/api/**` route handlers; shared logic in `src/lib/` (Prisma client, JWT, order/batch auth, DPP token helpers, VC builders, key management). **`middleware.ts`** gates `/api/*` except onboarding, auth, metadata, and `/api/public/*`.
- **Frontend**: `src/app/core/` (services, guards, models), `src/app/features/` (auth, dashboard, company, orders, batches, DPP display, public verification). Routes use **lazy `loadComponent`** to keep bundles small.
- **Data model**: **Company-centric** users (`User.companyId`, `SUPER_ADMIN` without company). Rich enums for compliance, batch lifecycle, and certificate linking via **`BatchCertificateLink`** (company certs, supplier certs, or uploads). **`DppRecord`** composite PK `(companyId, orderId, batchId)` ties the public passport to the operational batch.

## Engineering challenges

1. **Interoperable DPP data**: Shaping passport payloads as **JSON-LD** and **VC/VP** so consumers can verify integrity and issuer identity, not only render a pretty page.
2. **Deterministic signing**: **RFC 8785**-style canonical JSON before signing so signatures remain stable across serializers and platforms.
3. **Token evolution**: Supporting **new opaque DPP tokens** while **validating and migrating behavior** for older JWT-embedded links (`verifyDppToken` + DB lookup by claims).
4. **Key lifecycle**: Generating and storing **signing keys per company** with **encrypted private keys** at rest, and using them only when issuing credentials for that company’s data.
5. **Public vs authenticated surface**: Clear split between **middleware-whitelisted public routes** (onboarding, public DPP, platform key) and **Bearer-protected** company operations (orders, batches, certificate wiring).
6. **Complex relational domain**: Many-to-many style compliance requirements per order, per batch, with **link rows** tracking pending vs linked vs waived certificates without duplicating cert blobs.
7. **Batch → minted DPP**: State transitions (e.g. verification decision) that **atomically** update batch flags, tokens, mint timestamps, and **`DppRecord`** snapshots for a consistent public read model.

---

*Tailor the “What I built” section to your actual role (solo vs team); replace with concrete metrics or deployments if you have them.*
