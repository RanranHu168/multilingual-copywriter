def generate_prompt(product, features, tone, lang):
    tone_dict = {
        "Formal": {"English": "professional", "中文": "正式", "Français": "formel"},
        "Enthusiastic": {"English": "enthusiastic", "中文": "热情", "Français": "enthousiaste"},
        "Playful": {"English": "playful", "中文": "俏皮", "Français": "enjoué"},
    }
    style = tone_dict[tone][lang]

    templates = {
        "English": f"Write a {style} product description for a product named '{product}', with features: {features}.",
        "中文": f"请以{style}的语气，撰写一个名为“{product}”的产品文案，特点包括：{features}。",
        "Français": f"Rédige une description de produit en style {style} pour un produit nommé '{product}', avec les caractéristiques suivantes : {features}.",
    }

    return templates[lang]
