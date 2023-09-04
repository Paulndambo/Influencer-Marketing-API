def utm_constructor(url, campaign):
    medium = "social"
    content = "olitt_promo"
    term = "new_stock"
    
    tiktok = f"{url}?utm_source=tiktok&utm_medium={medium}&utm_campaign={campaign}&utm_content={content}&utm_term={term}"
    facebook = f"{url}?utm_source=facebook&utm_medium={medium}&utm_campaign={campaign}&utm_content={content}&utm_term={term}"
    twitter = f"{url}?utm_source=twitter&utm_medium={medium}&utm_campaign={campaign}&utm_content={content}&utm_term={term}"
    instagram = f"{url}?utm_source=instgram&utm_medium={medium}&utm_campaign={campaign}&utm_content={content}&utm_term={term}"
    youtube = f"{url}?utm_source=youtube&utm_medium={medium}&utm_campaign={campaign}&utm_content={content}&utm_term={term}"
    threads = f"{url}?utm_source=threads&utm_medium={medium}&utm_campaign={campaign}&utm_content={content}&utm_term={term}"
    email = f"{url}?utm_source=email&utm_medium={medium}&utm_campaign={campaign}&utm_content={content}&utm_term={term}"
    snapchat = f"{url}?utm_source=snapchat&utm_medium={medium}&utm_campaign={campaign}&utm_content={content}&utm_term={term}"
    linkedin = f"{url}?utm_source=linkedin&utm_medium={medium}&utm_campaign={campaign}&utm_content={content}&utm_term={term}"
    
    return tiktok, facebook, twitter, instagram, youtube, threads, email, snapchat, linkedin

