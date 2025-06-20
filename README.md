# 🌍 Multilingual AI Copywriting Tool

> Generate persuasive product descriptions in English, Chinese, and French — tailored to tone, language, and user intent.  
> 🚀 Built with OpenAI GPT-4 + Streamlit + Prompt Engineering

---

## ✨ Overview

Modern e-commerce demands fast, high-quality, multilingual content that resonates with diverse global audiences. This tool allows users to generate **customized product copy** in **three languages** with varied writing tones — all powered by a single click.

Whether you're launching a brand on Amazon, building a Shopify store, or testing product-market fit, this tool empowers **non-technical users** to instantly generate polished, emotionally aligned marketing copy.

---

## 🎥 Live Demo

Here’s a quick look at how it works 👇  
![Demo](Screenshot.gif)

---

## 🔥 Use Case Example

**Input:**

- Product: `Natural Amethyst Crystal Pendant`  
- Features: `100% natural, hand-polished, calming energy, elegant design`  
- Tone: `Enthusiastic`  
- Languages: `English, 中文, Français`

**Output:**

> ✨ *[English]*  
> Radiate elegance and tranquility with our Natural Amethyst Crystal Pendant! Hand-polished from 100% natural amethyst, this pendant isn’t just a stunning accessory — it’s a symbol of inner peace and refined taste.

> ✨ *[中文]*  
> 用我们的天然紫水晶吊坠点亮你的优雅气场！精选100%天然紫水晶，纯手工打磨，每一件都蕴含安抚情绪的能量，是每日穿搭中不可或缺的灵气之选。

> ✨ *[Français]*  
> Brillez avec élégance et sérénité grâce à notre pendentif en cristal d'améthyste naturel, taillé à la main à partir d’améthyste 100 % naturelle.

---

## 🧩 Key Features

✅ Generate product copy in **English**, **Chinese**, and **French**  
✅ Choose writing tone: `Formal`, `Enthusiastic`, or `Playful`  
✅ Built with **OpenAI GPT-4 API**  
✅ Web-based interface using **Streamlit**  
✅ Lightweight and deployable in under 1 minute  
✅ Multilingual prompt engineering and tone control

---

## 🎯 Why This Project Matters

> “Anyone can call an API — but few can **design delightful tools** that solve real business problems.”

This project demonstrates my ability to:

- ⚙️ Integrate large language models (LLMs) into usable applications
- 🧠 Engineer prompts for **controlled outputs** across tone and language
- 🎨 Design **non-technical-friendly interfaces** with Streamlit
- 🌐 Handle multilingual UX challenges (UTF-8, language-specific context, style)
- 💼 Build tools that align with **real-world market use cases**

---

## 🛠️ Tech Stack

| Layer        | Technology              |
|--------------|--------------------------|
| UI           | Streamlit                |
| LLM API      | OpenAI GPT-4             |
| Env Mgmt     | python-dotenv            |
| Language Logic | Custom Prompt Templates |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourname/multilingual-copywriter.git
cd multilingual-copywriter
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up your OpenAI API key
Create a .env file and paste:

```env
OPENAI_API_KEY=your_openai_api_key
```

### 4. Run the app

```bash
streamlit run multilingual_copywriter.py
```

##  Project Structure
```bash
multilingual_copywriter/
├── app.py             # Main Streamlit app
├── prompts.py         # Prompt generation logic
├── openai_api.py      # OpenAI GPT-4 integration
├── .env               # API key config (not committed)
├── requirements.txt   # Python dependencies
└── README.md          # This file

```

## Future Improvements

 - Add export-to-CSV / Word / PDF functionality

 - Support for more languages (Spanish, German, Japanese)

 - Fine-tuned tone sliders (e.g. 0–100 between Formal and Playful)

 - User authentication + copy history tracking

 - Image-to-copy: Generate descriptions from uploaded product photos


##  Author’s Note

This is a showcase of how LLMs can power real-world content tools — with minimal effort from the user. I designed this app to explore:

AI usability in commerce & copywriting

Practical prompt engineering strategies

Scalable multilingual content pipelines

If you're hiring for roles in AI product development, prompt design, or LLM integration — let's talk. I’m passionate about building tools that bridge deep tech with human needs.

## 📬 Contact

- Ranran Hu
- Email: huranran8@gmail.com
- GitHub: github.com/RanranHu168
- LinkedIn: https://www.linkedin.com/in/ranran-hu-303154152/

## ⭐️ If you found this project useful or inspiring, please give it a star on GitHub!
