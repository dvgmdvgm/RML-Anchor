# 🧠 Système de Mémoire IA (RLM-Anchor)

> **Mémoire à long terme inspirée de RLM pour assistants IA**

Un système de mémoire persistante pour les environnements de développement propulsés par l'IA, basé sur les principes des [Recursive Language Models](https://arxiv.org/abs/2512.24601) (voir [Guide Vidéo](https://www.youtube.com/watch?v=huszaaJPjU8)).

---

## 🌟 Caractéristiques

- **📁 13 catégories organisées** — stockage structuré de toutes les connaissances du projet
- **🔍 Recherche de type RLM** — Examine → Decompose → Recurse → Aggregate
- **🌍 Support multilingue** — réponses et enregistrements dans n'importe quelle langue
- **⚡ Commandes simples** — `/remember`, `/recall`, `/wakeup`, `/sleep`
- **🔄 Persistance de session** — contexte préservé entre les sessions
- **📝 Basé sur Markdown** — lisible par l'homme, compatible Git

---

## 📦 Quick Start & Usage

1. **Importez le dossier `.agent/`** dans votre projet avec Git :
   ```bash
   git clone --depth 1 https://github.com/dvgmdvgm/AnchorGravity.git .temp && cp -r .temp/.agent . && rm -rf .temp
   ```
2. **Réglez votre langue** dans le fichier `.agent/memory/13_preferences/language.md`.
3. **Exécutez exactement ce prompt :** ```/anchor_agent scannez les répertoires du projet actuel pour trouver des données qui aideront à construire le contexte et à configurer la mémoire correctement (données techniques, modèles commerciaux, règles de conception et tous les autres modèles typiques pour trouver et préserver le contexte du projet)``` pour implémenter RLM-Anchor en toute sécurité dans votre projet actuel.
4. **Commencez à travailler** avec la commande de chat ```/wakeup```.
5. **Travaillez dans votre IDE** (développement, résolution de tâches, décisions commerciales, comme d'habitude).

*Au cours du travail, vous pouvez utiliser* ```/remember``` *pour sauvegarder le contexte important.*

6. **Une fois le travail terminé**, par exemple avant de dormir, exécutez la commande ```/sleep``` pour que RLM-Anchor puisse sauvegarder votre contexte en mémoire.

*Chaque fois que vous reprenez le travail, réveillez RLM-Anchor avec* ```/wakeup``` *et à la fin, renvoyez-le dormir avec* ```/sleep``` *pour qu'il mémorise tout votre travail.*

---

## 🌍 Configuration de la langue

Modifiez `.agent/memory/13_preferences/language.md` :

```
LANGUAGE=fr    # Français
LANGUAGE=en    # Anglais
...
```

---

## ⚡ Commandes

| Commande | Description |
|----------|-------------|
| `/wakeup` | Démarrer la session, charger le contexte |
| `/sleep` | Terminer la session, résumer le travail |
| `/remember` | Enregistrer des informations en mémoire |
| `/recall` | Rechercher des informations en mémoire |
| `/handoff` | Créer un résumé pour changer de modèle |
| `/walkthrough` | Générer la documentation d'une fonctionnalité |
| `/anchor_agent` | Intégration sécurisée dans le projet |
| `/memory-stats` | Afficher les statistiques de mémoire |

---

## 🙏 Crédits
Inspiré par les [recherches RLM du MIT](https://arxiv.org/abs/2512.24601) sur les modèles de langage récursifs et [ce guide vidéo](https://www.youtube.com/watch?v=huszaaJPjU8).
