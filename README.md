<div align="center">

<!-- Animated Storytelling Terminal Header -->
<img src="assets/terminal.svg" alt="Yashika Agrawal - Interactive Developer Terminal" width="100%"/>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=15&duration=2800&pause=1000&color=38BDF8&center=true&vCenter=true&multiline=true&width=620&height=48&lines=%24+dotnet+build+fullstack-apps...;%24+npm+run+dev%3Areact-frontend...;%24+provisioning+isolated+Linux+VMs+with+Multipass..." alt="Live typing terminal" />
</p>

**Software Engineer · Full Stack Development**

*I build full-stack web applications, explore how systems work under the hood, and turn what I learn into experiments.*

[![GitHub](https://img.shields.io/badge/GitHub-Yashika--Agrawal-161b22?style=flat-square&logo=github)](https://github.com/Yashika-Agrawal)
[![Email](https://img.shields.io/badge/Email-Get%20in%20touch-161b22?style=flat-square&logo=gmail)](mailto:yashikayash2002@gmail.com)

</div>

---

## `~/lab/live-pulse`

<!-- LAB:START -->
| Area | Live Pulse |
|---|---|
| 🚀 **Active Repos** | [Engineering-playground](https://github.com/Yashika-Agrawal/Engineering-playground) · [Ananta](https://github.com/Yashika-Agrawal/Ananta) · [neetcode-submissions](https://github.com/Yashika-Agrawal/neetcode-submissions) |
| 📝 **Latest Note** | [Azure Key Vault](https://github.com/Yashika-Agrawal/Engineering-playground/blob/main/azure/ai-200/azure-key-vault.md) (`azure/ai-200`) |
| 🕒 **Latest Commit** | [`114e49e`](https://github.com/Yashika-Agrawal/Engineering-playground/commit/114e49ebb0cdea9584e5d9def26dc3d80175716d) docs: add Azure Key Vault guide and update container deployment not… (`Engineering-playground`) |
<!-- LAB:END -->

---

## `~/playground-matrix`

> A clickable constellation of hands-on experiments from [`Engineering-playground`](https://github.com/Yashika-Agrawal/Engineering-playground). Click any link to jump straight into the notes:

<!-- MATRIX:START -->
| Domain | Notes & Experiments |
|:---|:---|
| 📂 **Azure** | [`ACR-tasks.md`](https://github.com/Yashika-Agrawal/Engineering-playground/blob/main/azure/ai-200/ACR-tasks.md) · [`ai-agents.md`](https://github.com/Yashika-Agrawal/Engineering-playground/blob/main/azure/ai-200/ai-agents.md) · [`azure-container-registry.md`](https://github.com/Yashika-Agrawal/Engineering-playground/blob/main/azure/ai-200/azure-container-registry.md) · [`azure-key-vault.md`](https://github.com/Yashika-Agrawal/Engineering-playground/blob/main/azure/ai-200/azure-key-vault.md) · [`containers.md`](https://github.com/Yashika-Agrawal/Engineering-playground/blob/main/azure/ai-200/containers.md) · [`deploying-container-to-azure-web-app.md`](https://github.com/Yashika-Agrawal/Engineering-playground/blob/main/azure/ai-200/deploying-container-to-azure-web-app.md) · [`docker-to-acr.md`](https://github.com/Yashika-Agrawal/Engineering-playground/blob/main/azure/ai-200/docker-to-acr.md) · [`fundamentals.md`](https://github.com/Yashika-Agrawal/Engineering-playground/blob/main/azure/ai-200/fundamentals.md) · [`microsoft-foundry.md`](https://github.com/Yashika-Agrawal/Engineering-playground/blob/main/azure/ai-200/microsoft-foundry.md) |
| 📂 **DevOps** | [`intro-to-ci-cd.md`](https://github.com/Yashika-Agrawal/Engineering-playground/blob/main/Devops/Ci-Cd/intro-to-ci-cd.md) · [`intro-to-devops.md`](https://github.com/Yashika-Agrawal/Engineering-playground/blob/main/Devops/intro-to-devops.md) · [`multipass.md`](https://github.com/Yashika-Agrawal/Engineering-playground/blob/main/Devops/multipass.md) |
| 📂 **Networking** | [`browser-page-load.md`](https://github.com/Yashika-Agrawal/Engineering-playground/blob/main/networking/browser-page-load.md) · [`content-type-and-www.md`](https://github.com/Yashika-Agrawal/Engineering-playground/blob/main/networking/content-type-and-www.md) |
<!-- MATRIX:END -->

---

## `~/projects`

<div align="center">

| Project | What I Built | Stack |
|---|---|---|
| [**Pollify**](https://github.com/Yashika-Agrawal/pollify) | Real-time polling web application with live voting results and instant state synchronization across clients. | React · Node.js · PostgreSQL · Prisma · Socket.IO |
| [**Live Tracker**](https://github.com/Yashika-Agrawal/live-tracker) | Real-time vehicle location streaming on interactive maps with live coordinate broadcast. | Express · Socket.IO · Docker · Leaflet |

</div>

<br/>

### 🛠️ Full-Stack Architecture Deep-Dive
*(Click to expand the technical flow)*

<details open>
<summary><b>🔍 View: Pollify Full-Stack Architecture (Real-Time State Sync)</b></summary>
<br/>

```text
[ React + Tailwind Frontend ]
         │
         │  (1) Cast Vote / Create Poll
         ▼
[ Express.js + Node.js API Gateway ]
         │
         ├──► (2) Persist Vote ──► [ Prisma ORM ] ──► [ PostgreSQL ]
         │
         │    (3) Broadcast Live Tally (Event Emit)
         ▼
[ Socket.IO Real-Time Server ]
         │
         ▼
[ All Connected Client UIs Updated Instantly ]
```

* **Core Focus:** Ensuring database persistence through Prisma transactions while broadcasting live vote aggregates to connected clients via WebSockets with minimal latency.

</details>

---

## `~/toolbox`

| Layer | Technologies & Tools |
|---|---|
| **Frontend** | React · JavaScript · TypeScript · Tailwind CSS · HTML5 / CSS3 |
| **Backend & APIs** | C# · .NET · ASP.NET Core · Node.js · Express · REST APIs |
| **Data & Databases** | PostgreSQL · SQL · MongoDB · Prisma ORM |
| **Infra & DevOps** | Docker · Linux · Multipass · Git · GitHub Actions · CI/CD · AWS |

---

<div align="center">

**Always learning. Always building. Always curious.**

`console.log("Thanks for stopping by 👋");`

</div>
