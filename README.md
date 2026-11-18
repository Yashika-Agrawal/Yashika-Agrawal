<div align="center">

<!-- Animated Storytelling Terminal Header -->
<img src="assets/terminal.svg" alt="Yashika Agrawal - Interactive Developer Terminal" width="100%"/>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=15&duration=2800&pause=1000&color=38BDF8&center=true&vCenter=true&multiline=true&width=620&height=48&lines=%24+dotnet+build+backend-services...;%24+streaming+events+with+Kafka+%26+Socket.IO...;%24+provisioning+isolated+Linux+VMs+with+Multipass..." alt="Live typing terminal" />
</p>

**Software Engineer · Backend & Systems · Cloud & DevOps**

*Building web applications, exploring how systems work under the hood, and turning every bug into an experiment.*

[![GitHub](https://img.shields.io/badge/GitHub-Yashika--Agrawal-161b22?style=flat-square&logo=github)](https://github.com/Yashika-Agrawal)
[![Email](https://img.shields.io/badge/Email-Get%20in%20touch-161b22?style=flat-square&logo=gmail)](mailto:yashikayash2002@gmail.com)

</div>

---

## `~/lab/live-pulse`

<!-- LAB:START -->
| Area | Current Focus / Live Pulse |
|---|---|
| 🚀 **Building** | RailRush (.NET 8 & PostgreSQL) |
| 🔍 **Exploring** | Linux & OS Internals · Concurrency & Transactions · DevOps & CI/CD Automation |
| 🧪 **Latest Experiment** | [Local Linux VMs & SSH key authentication with Multipass](https://github.com/Yashika-Agrawal/Engineering-playground/blob/main/Devops/multipass.md) |
| 📝 **Engineering Note** | [CI/CD Pipeline Automation: Builds, Triggers & Runners](https://github.com/Yashika-Agrawal/Engineering-playground/blob/main/Devops/Ci-Cd/intro-to-ci-cd.md) |
| 💡 **Today I Learned** | [Why SSH prints host key authenticity warning on first connect (Host verification vs client key pairs)](https://github.com/Yashika-Agrawal/Engineering-playground/blob/main/Devops/multipass.md) |
<!-- LAB:END -->

> ⚡ *This section is kept alive automatically by [`scripts/update_lab.py`](scripts/update_lab.py) and GitHub Actions.*

---

## `~/playground-matrix`

> A clickable constellation of hands-on experiments from [`Engineering-playground`](https://github.com/Yashika-Agrawal/Engineering-playground). Click any link to jump straight into the code or notes:

| Domain | Focus Areas & Hands-On Experiments | Direct Links |
|:---|:---|:---|
| 🐧 **DevOps & Linux** | Local Ubuntu VMs, Multipass, SSH port 22 security groups, host key verification, firewall rules | [`multipass.md`](https://github.com/Yashika-Agrawal/Engineering-playground/blob/main/Devops/multipass.md) |
| 🔄 **CI/CD Automation** | Pipeline architecture, automated build/test gates, GitHub Actions runner isolation | [`intro-to-ci-cd.md`](https://github.com/Yashika-Agrawal/Engineering-playground/blob/main/Devops/Ci-Cd/intro-to-ci-cd.md) |
| ⚡ **Real-Time & Events** | Event streaming with Apache Kafka, real-time WebSockets, handling telemetry bursts | [`live-tracker`](https://github.com/Yashika-Agrawal/live-tracker) · [`pollify`](https://github.com/Yashika-Agrawal/pollify) |
| 🚆 **Backend & Data** | Database modeling, concurrency control, avoiding double-bookings with row locks (.NET 8 & PostgreSQL) | [`RailRush`](https://github.com/Yashika-Agrawal/RailRush) |
| 🛠️ **System Fundamentals** | Linux daemons, system services, DNS, client-server lifecycle | [`intro-to-devops.md`](https://github.com/Yashika-Agrawal/Engineering-playground/blob/main/Devops/intro-to-devops.md) |

---

## `~/projects`

<div align="center">

| Project | What I'm Building | Stack |
|---|---|---|
| **RailRush** | A railway reservation system exploring ACID transactions, concurrency locking, and booking flows. | C# · .NET 8 · PostgreSQL · EF Core |
| [**Live Tracker**](https://github.com/Yashika-Agrawal/live-tracker) | Real-time vehicle location streaming with partitioned event queues to decouple ingest from broadcast. | Express · Socket.IO · Apache Kafka · Docker |
| [**Pollify**](https://github.com/Yashika-Agrawal/pollify) | Real-time polling application with instant state sync across connected clients. | React · Node.js · PostgreSQL · Prisma · Socket.IO |

</div>

<br/>

### 🛠️ Interactive System Architecture Deep-Dives
*(Click to expand the technical breakdown of each system)*

<details>
<summary><b>🔍 View: Live Tracker Architecture (Event-Driven Stream)</b></summary>
<br/>

```text
[ Leaflet Client (Browser) ]
         │
         │  (WebSockets / Socket.IO)
         ▼
[ Express.js Gateway ]
         │
         │  (Producer Event)
         ▼
[ Apache Kafka Cluster ] ──► [ Topic: vehicle-coordinates ]
         │
         │  (Consumer Stream)
         ▼
[ Dockerized Service Worker ] ──► Real-Time Broadcast & Spatial Processing
```

* **Engineering Decision:** Decoupled telemetry ingestion from client broadcasts using Kafka to prevent WebSocket gateway bottlenecks during coordinate bursts.

</details>

<details>
<summary><b>🔍 View: RailRush Reservation & Concurrency Flow</b></summary>
<br/>

```text
[ Booking Request ] ──► [ ASP.NET Core Web API ] ──► [ EF Core Transaction ]
                                                              │
                                                              ▼
                                                    [ Row-Level DB Lock ]
                                                    (Prevents Double Booking)
                                                              │
                                                              ▼
                                                    [ PostgreSQL Commit ]
```

* **Engineering Decision:** Exploring ACID transaction isolation levels and concurrency control to handle simultaneous ticket bookings safely under high contention.

</details>

---

## `~/things-i-got-wrong`

<details open>
<summary><b>💡 Bugs, Misconceptions & What I Learned Under the Hood</b></summary>
<br/>

- **SSH Host Verification vs Client Keys (Linux / Multipass):**  
  *The Mistake:* When SSH threw `The authenticity of host '192.168.252.2' can't be established`, I initially thought my local Mac SSH key wasn't loaded.  
  *The Reality:* SSH verifies the identity of the **server** (host key fingerprint) before sending client credentials to prevent Man-in-the-Middle attacks. Once accepted, it is permanently pinned in `~/.ssh/known_hosts`.

- **In-Memory Locks in Distributed Backends (.NET / PostgreSQL):**  
  *The Mistake:* Using C# memory locks (`lock (seatObj)`) to prevent concurrent double-booking in a reservation system.  
  *The Reality:* Memory locks only protect a single process on a single machine. The moment the backend scales across multiple containers or instances, transactions collide. True safety requires database-level row locks (`SELECT FOR UPDATE`) or serializable isolation.

- **Direct WebSocket Broadcast under Traffic Bursts:**  
  *The Mistake:* Emitting raw location telemetry straight to all connected WebSocket clients from the API route.  
  *The Reality:* Under coordinate spikes, the event loop chokes and frames drop. Inserting an Apache Kafka broker between ingestion and consumption buffers bursts smoothly without dropping packets.

</details>

---

## `~/toolbox`

| Layer | Technologies & Tools |
|---|---|
| **Backend & APIs** | C# · .NET · ASP.NET Core · Node.js · Express · REST APIs |
| **Data & Messaging** | PostgreSQL · SQL · MongoDB · Prisma · Apache Kafka |
| **Frontend** | React · JavaScript · TypeScript · Tailwind CSS |
| **Infra & DevOps** | Docker · Linux · Multipass · Git · GitHub Actions · CI/CD · AWS |

---

## `~/contributions`

<div align="center">

<!-- 3D Isometric Contribution Skyline (Falls back to snake if pending first run) -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="profile-3d-contrib/profile-night-rainbow.svg">
  <img src="profile-3d-contrib/profile-night-rainbow.svg" alt="3D Isometric Contribution Skyline" width="100%" onerror="this.style.display='none'"/>
</picture>

<img src="https://raw.githubusercontent.com/Yashika-Agrawal/Yashika-Agrawal/output/github-contribution-grid-snake-dark.svg" alt="GitHub contribution snake animation" width="100%"/>

</div>

---

<div align="center">

**Always learning. Always building. Always curious.**

`console.log("Thanks for stopping by 👋");`

</div>
