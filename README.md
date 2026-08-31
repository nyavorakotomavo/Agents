# Autonomous Agents with CrewAI & GitHub Actions

Ce projet est un template/base pour exécuter des agents autonomes avec **CrewAI**, exposés via une API REST avec **FastAPI**, et automatisés via **GitHub Actions**.

## 🚀 Fonctionnalités

- **CrewAI** : Structure multi-agents (Research Analyst + Content Strategist).
- **FastAPI** : Endpoint REST `/run-crew` pour déclencher les agents sur un sujet donné.
- **GitHub Actions** :
  - Intégration Continue (CI) : exécution automatique des tests unitaires (`pytest`) lors des pushs / PRs.
  - Exécution programmée ou manuelle (`workflow_dispatch`) des agents autonomes via GitHub Actions avec export de secrets (`OPENAI_API_KEY`).

---

## 🛠️ Configuration & Installation Locale

1. **Cloner le dépôt** et installer les dépendances :

```bash
pip install -r requirements.txt
```

2. **Variables d'environnement** :
Créez un fichier `.env` ou définissez la clé API OpenAI dans votre terminal :

```bash
export OPENAI_API_KEY="votre-cle-openai"
```

3. **Lancer le serveur API FastAPI** :

```bash
uvicorn main:app --reload
```

L'API sera disponible sur `http://127.0.0.1:8000`. Vous pouvez tester les endpoints suivants :
- `GET /` : Vérifier que l'API fonctionne.
- `GET /health` : Monitoring health check.
- `POST /run-crew` : Déclencher les agents autonomes.
  ```json
  {
    "topic": "AI Automation in Software Engineering"
  }
  ```

4. **Exécuter directement la Crew en CLI** :

```bash
python crew.py
```

---

## 🧪 Tests Unitaires

Pour lancer l'ensemble des tests de l'application :

```bash
pytest
```

---

## 🤖 Automatisations GitHub Actions

Le workflow `.github/workflows/ci.yml` gère deux rôles :

1. **Test Job** : Se déclenche automatiquement lors des `push` et `pull_request` sur les branches `main` / `master`.
2. **Run Agent Job** :
   - **Manuel** : Déclenchable depuis l'onglet *Actions* de GitHub (*Run workflow*) en renseignant un sujet (`topic`).
   - **Planifié (CRON)** : Exécution automatique quotidienne (par défaut à minuit).

> **Note :** Pensez à ajouter votre clé `OPENAI_API_KEY` dans les secrets de votre dépôt GitHub (`Settings > Secrets and variables > Actions`).
