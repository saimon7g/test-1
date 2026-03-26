# Hope — Healthcare mobile client (Flutter)

## What it is

**Hope** is a cross-platform Flutter app for a healthcare platform: **patients** discover providers, manage bookings, prescriptions, and vitals; **providers** (caregivers and doctors) run a multi-tab workspace for jobs, scheduling, profile/verification, wallet, and service analytics.

## What I built / shipped

- **Authentication & session**: login, sign-up flows (patient vs provider), OTP verification, forgot/reset password, JWT-backed sessions with restore-on-launch and role-aware post-login routing.
- **Patient experience**: shell navigation (Home, Discover, Liked, Bookings, Profile) using a state-preserving tab pattern; booking, reviews, doctor discovery, prescriptions, and vitals-related UI wired to backend services.
- **Provider experience**: caregiver dashboard with **Dashboard**, **Jobs** (shifts, clinical/review flows), **Schedule** (calendar, slots, agenda), **Profile** (editable sections, verification, services, billing), and **Wallet** (transactions, KPI-style summaries); mode handling for caregiver vs doctor/specialist based on stored provider metadata.
- **Platform integrations**: Firebase Cloud Messaging (permissions, token lifecycle, background handler, device registration against the API), geolocation for location-aware flows, file picking and multipart uploads to a dedicated upload base URL.
- **Shared infrastructure**: centralized HTTP client, dependency injection and route bindings, global loading UX, and consistent theming (Material 3).

## Stack

| Area | Choices |
|------|---------|
| Framework | Flutter, Dart ^3.6 |
| State, routing, DI | GetX (`GetMaterialApp`, `GetPage`, `Bindings`, controllers) |
| Networking | Dio (timeouts, interceptors, JSON & `FormData`) |
| Persistence | GetStorage (tokens, user model, flags) |
| Push | `firebase_core`, `firebase_messaging` |
| Device / files | `device_info_plus`, `file_picker` |
| Auth helpers | `jwt_decoder` |
| Charts / UX | `fl_chart`, `flutter_easyloading`, `logger`, `intl`, `url_launcher` |
| Location | `geolocator` |

## Architecture & project structure

Layered layout under `lib/`:

- **`route/`** — Declarative routes (`AppRouter`) and named `GetPage`s with optional bindings.
- **`bindings/`** — Registers long-lived `ApiClient` and lazy feature services/controllers (e.g. dashboard → vitals, liked providers).
- **`controllers/`** — GetX controllers for auth, bookings, search, notifications, location, etc.
- **`services/`** — Feature services (auth, schedule, wallet, reviews, consultations, …) plus a shared **`api-client/`** `ApiClient` abstraction; some domains expose small **`i-*.dart`** interfaces.
- **`data/models/`** — Request/response and domain DTOs aligned with API shapes.
- **`data/constants/`** — App config (base URLs, API version segment, keys).
- **`views/screens/`** & **`views/widgets/`** — Screens and composable widgets (auth, patient, caregiver, payment dialog, etc.).
- **`utils/`** — Helpers and session logout utilities decoupled from UI.

**Patterns:** service → controller → view; API access funneled through `ApiClient`; bindings keep registration idempotent (`Get.isRegistered`) where needed.

## Engineering challenges

1. **Multi-role product surface** — One codebase serves patient and provider journeys with different shells, routes, and bindings; provider UI further branches caregiver vs doctor behavior from persisted category/type metadata.
2. **Robust auth on the wire** — Interceptors attach Bearer tokens, detect **expired JWTs** before requests, and clear session on **401**; optional **temporary** `Authorization` headers support flows that need a different token without polluting the default session.
3. **Two backends from one client** — Versioned REST base URL plus a **separate file-upload host** and multipart helpers (single, multi-file, patch-vs-post).
4. **Push reliability** — FCM init, permission UX, token refresh re-registration, and a **top-level** background message handler to satisfy Flutter/Firebase constraints.
5. **Session continuity** — Restore user JSON and token after restart; re-hydrate `ApiClient` headers so the next API call is already authenticated.

---

*Use this file as portfolio copy; adjust wording (e.g. team vs solo) to match how you present the work.*
