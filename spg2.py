# SPG Version 2.0 by https://t.me/anonymousWindia

import os
import random

def collect_inputs():
    print("🔐 SPG Version 2.0 by https://t.me/anonymousWindia\n")

    victim_name = input("👤 Victim name: ").strip().lower()
    victim_age = input("🎂 Age (press Enter to skip): ").strip()
    dob = input("📆 DOB (dd/mm/yyyy) (Enter to skip): ").strip()

    has_partner = input("❤️ Victim has GF/BF/Crush? (y/n): ").strip().lower()
    partner_name = input("💞 Partner name: ").strip().lower() if has_partner == "y" else ""

    has_idol = input("⭐ Victim has any idol/celebrity they follow? (y/n): ").strip().lower()
    idol_name = input("📣 Idol name (e.g. dhoni, thala, king): ").strip().lower() if has_idol == "y" else ""

    if victim_age.isdigit() and int(victim_age) < 20:
        city = input("🏙️ City (Enter to skip): ").strip().lower()
        country = input("🌍 Country (Enter to skip): ").strip().lower()
    else:
        city, country = "", ""

    return {
        "victim": victim_name,
        "partner": partner_name,
        "idol": idol_name,
        "dob": dob.replace("/", ""),
        "age": victim_age or "18",
        "city": city,
        "country": country
    }

def generate_passwords(data, max_count=10000):
    name = data["victim"]
    partner = data["partner"]
    idol = data["idol"]
    dob = data["dob"]
    age = data["age"]
    city = data["city"]
    country = data["country"]

    common_nums = ["07", "407", "143", "786", "999", "123", "321", "2231", "1023", "1001", dob[-4:] if dob else ""]
    years = ["2023", "2024", "2025", "2026", dob[-4:] if dob else ""]
    keywords = ["love", "lover", "crush", "forever", "king", "queen", "thala", "fan", "only", "boss", "crazy", "obsessed"]
    final = set()

    components = [name]
    if partner: components.append(partner)
    if idol: components.append(idol)

    tries = 0
    while len(final) < max_count and tries < max_count * 3:
        base = random.choice(components)
        second = random.choice(components)
        key = random.choice(keywords)
        num = random.choice(common_nums + years)
        sep = random.choice(["_", ".", "-", ""])

        pattern = random.choice([
            f"{base}{sep}{key}{sep}{num}",
            f"{base}{sep}{num}",
            f"{base}{sep}{second}{sep}{num}",
            f"{base}{sep}{second}{sep}{key}",
            f"{key}{sep}{base}{sep}{num}",
            f"{base}{sep}{key}",
            f"{second}{sep}{base}{sep}{num}",
            f"{base}{sep}the{sep}{key}",
            f"{base}{sep}fan{sep}{idol}",
            f"{base}{sep}{partner}{sep}143",
        ])

        if city:
            if random.random() < 0.3:
                pattern += sep + random.choice([city, country])

        final.add(pattern.lower())
        tries += 1

    return sorted(final)

def save_to_file(passwords, victim_name):
    save = input("\n💾 Do you want to save the wordlist to file? (y/n): ").strip().lower()
    filename = f"{victim_name}_wordlist.txt"

    if not os.path.exists("output"):
        os.makedirs("output")

    with open(f"output/{filename}", "w") as f:
        for pw in passwords:
            f.write(pw + "\n")

    if save == 'y':
        print(f"\n✅ Saved as output/{filename}")
    else:
        print(f"\n😏 You said no, but I saved it anyway.")
        print(f"📁 Auto-saved as output/{filename}")

def main():
    data = collect_inputs()
    pw_list = generate_passwords(data, max_count=5000)

    print(f"\n🧠 {len(pw_list)} smart human-style passwords generated.\n\n🔎 Some samples:")
    for pw in list(pw_list)[:30]:
        print(f" - {pw}")
    
    save_to_file(pw_list, data['victim'])

if __name__ == "__main__":
    main()
