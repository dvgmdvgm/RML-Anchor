# 🧠 Système de Mémoire IA (RLM-Anchor)

> **Mémoire à long terme pour assistants IA basée sur RLM**

Un système de mémoire persistante pour les environnements de développement IA, basé sur les principes des [Recursive Language Models](https://arxiv.org/abs/2512.24601) (recherche MIT) (voir [Guide vidéo](https://www.youtube.com/watch?v=huszaaJPjU8)).

> Donnez à votre assistant IA une **mémoire persistante** qui survit entre les sessions de chat.

---

## 💡 Le Problème

Chaque fois que vous démarrez un nouveau chat avec une IA, elle oublie tout :
- L'architecture du projet
- Les décisions passées et leurs raisons
- Les bugs connus et solutions de contournement
- Votre style de programmation
- Ce sur quoi vous avez travaillé hier

**RLM-Anchor résout ce problème.** Il donne à l'IA une mémoire structurée à long terme — sous forme de simples fichiers Markdown directement dans votre projet.

---

---

## 🌟 Fonctionnalités

- **📁 13 catégories organisées** — stockage structuré des connaissances du projet
- **🔍 Recherche style RLM** — Examine → Decompose → Recurse → Aggregate
- **🌍 Multilingue** — réponses et entrées dans n'importe quelle langue
- **⚡ Commandes simples** — `/remember`, `/recall`, `/wakeup`, `/sleep`
- **🔄 Transfert de contexte** — basculement fluide entre modèles IA
- **📝 Basé sur Markdown** — lisible par les humains, compatible Git
- **🔄 Persistance des sessions** — le contexte est préservé entre les sessions

---

## 📦 Quick Start & Usage

> ⚠️ **IMPORTANT** : Chaque projet nécessite une installation SÉPARÉE de RLM-Anchor ! Utiliser une mémoire pour plusieurs projets confondra l'IA à cause de contextes conflictuels. Installez toujours à nouveau pour chaque nouveau projet.

1. **Importez le dossier `.agent/`** dans votre projet via Git :
   ```bash
   git clone --depth 1 https://github.com/dvgmdvgm/AnchorGravity.git .temp && cp -r .temp/.agent . && rm -rf .temp
   ```
2. **Définissez la langue** dans `.agent/memory/13_preferences/language.md`
3. **Exécutez ce prompt** (copiez le bloc entier) :
   ```
   /anchor_agent vérifie les répertoires du projet actuel pour les données qui aideront à construire le contexte et configurer la mémoire correctement (données techniques, modèles commerciaux, règles de conception et tous les autres modèles typiques pour trouver et préserver le contexte du projet)
   ```
4. **Commencez à travailler** avec la commande chat `/wakeup`.
5. **Travaillez dans votre IDE** (développement, résolution de problèmes, décisions commerciales, tout comme d'habitude).

*Pendant le travail, aux étapes importantes, vous pouvez utiliser* `/remember` *pour sauvegarder le contexte important.*

6. **Quand vous avez fini de travailler** dans l'IDE, par exemple avant de dormir, exécutez `/sleep` pour que RLM-Anchor sauvegarde le contexte en mémoire.

*Maintenant, chaque fois que vous revenez travailler sur le projet — réveillez simplement RLM-Anchor avec* `/wakeup` *et à la fin de la session renvoyez-le dormir* `/sleep` *pour qu'il se souvienne de tout ce que vous avez fait.*

---

## 🌍 Configuration de la Langue

Éditez `.agent/memory/13_preferences/language.md` :

```
LANGUAGE=fr    # Français
LANGUAGE=en    # Anglais
LANGUAGE=ru    # Russe  
...
```

---

## ⚡ Commandes

| Commande | Description |
|----------|-------------|
| `/wakeup` | Démarrer session, charger contexte |
| `/sleep` | Terminer session, archiver dans l'historique |
| `/remember` | Sauvegarder information en mémoire |
| `/recall` | Trouver information en mémoire |
| `/handoff` | Créer résumé pour changement de modèle |
| `/walkthrough` | Générer documentation de fonctionnalité |
| `/anchor_agent` | Intégration sécurisée au projet |
| `/anchor_briefing` | Briefing complet du projet (les 13 catégories) |
| `/anchor_backup` | Créer backup manuel (pour transfert) |
| `/anchor_restore` | Restaurer depuis backup ZIP |
| `/anchor_remove` | Suppression sécurisée du système (avec backup) |
| `/anchor_cleanup` | Nettoyage intelligent de mémoire (TTL, scoring) |
| `/anchor_update` | Mettre à jour vers dernière version depuis GitHub |
| `/anchor_validate` | Vérification d'intégrité de mémoire (5 vérifications) |
| `/memory-stats` | Afficher statistiques de mémoire avec tendances |

📖 **Documentation complète des commandes** : [COMMANDS.md](https://github.com/dvgmdvgm/AnchorGravity/blob/master/docs/COMMANDS.md)

---

## 📁 Structure

```
.agent/
├── MEMORY_INDEX.md           # Index principal de mémoire
├── skills/
│   └── MEMORY_SKILL.md       # Instructions pour IA
├── workflows/                 # Définitions de commandes
├── scripts/                   # Utilitaires Python
└── memory/
    ├── 01_project/           # Informations du projet
    ├── 02_architecture/      # Architecture système
    ├── 03_decisions/         # Décisions architecturales (ADR)
    ├── 04_domain/            # Domaine métier
    ├── 05_code/              # Documentation code
    ├── 06_problems/          # Problèmes et solutions
    ├── 07_context/           # Contexte des sessions
    ├── 08_people/            # Personnes et rôles
    ├── 09_external/          # Dépendances externes
    ├── 10_testing/           # Testing
    ├── 11_deployment/        # Déploiement
    ├── 12_roadmap/           # Plans et futur
    └── 13_preferences/       # Préférences et LANGUE
```

---

## 🔄 Comment ça Fonctionne

### Processus Style RLM

```
Requête utilisateur
    ↓
┌─────────────────────────────────────┐
│ 1. EXAMINE — Lire index mémoire     │
│ 2. DECOMPOSE — Déterminer catégories│
│ 3. RECURSE — Chercher dans fichiers │
│ 4. AGGREGATE — Combiner données     │
└─────────────────────────────────────┘
    ↓
Réponse contextuelle (dans langue configurée)
```

---

## 📝 Exemples d'Utilisation

### 🚀 Initialisation / Connexion
```
Utilisateur: /anchor_agent
IA: 📋 ANALYSE D'INTÉGRATION... [Scanne et propose options d'intégration sécurisée]
```

### ☀️ Démarrer Session
```
Utilisateur: /wakeup
IA: 🚀 Chargement du contexte projet...
    ✅ Session démarrée !
    📌 Tâches en attente : 2
```

### 📌 Sauvegarder Information
```
Utilisateur: /remember Nous avons choisi PostgreSQL pour les transactions ACID
IA: ✅ Sauvegardé dans memory/03_decisions/ADR-002-database.md
```

### 🔍 Rechercher Connaissances
```
Utilisateur: /recall Pourquoi avons-nous choisi PostgreSQL ?
IA: 📁 Trouvé en mémoire :
    Source : memory/03_decisions/ADR-002-database.md
    Nous avons choisi PostgreSQL pour le support des transactions ACID...
```

### 🔄 Transfert de Contexte (Handoff)
```
Utilisateur: /handoff
IA: 🔄 Création du résumé de transfert de contexte... [Génère résumé pour autre modèle]
```

### 📖 Génération de Documentation
```
Utilisateur: /walkthrough Nouvelle autorisation
IA: 📖 Walkthrough créé ! Sauvegardé dans memory/07_context/walkthroughs/2026-02-05_auth.md
```

### 📊 Statistiques Mémoire
```
Utilisateur: /memory-stats
IA: 📊 Statistiques : 42 fichiers, 13 catégories...
```

### 🌙 Terminer Session
```
Utilisateur: /sleep
IA: 📝 Résumé de la session...
    ✅ Historique sauvegardé.
    👋 À bientôt !
```

---

## 🛠️ Personnalisation

### Ajouter Nouvelles Catégories
1. Créer dossier dans `memory/`
2. Ajouter `_index.md` 
3. Mettre à jour `MEMORY_INDEX.md`

### Étendre Workflows
Éditez fichiers dans `workflows/` pour personnaliser commandes.

---

## 📄 Licence
MIT License — forkez et améliorez !

---

## 🙏 Remerciements
Inspiré par [recherche RLM du MIT](https://arxiv.org/abs/2512.24601) sur Recursive Language Models et [ce guide vidéo](https://www.youtube.com/watch?v=huszaaJPjU8).
