from playwright.sync_api import sync_playwright
from supabase import create_client

# -------- Supabase Configuration --------
url = "https://qeofwxcwkkxheodyvnfq.supabase.co"
key = "sb_publishable_rPR6HPjrKauOdKOW4uCg9w_MRcuQwQC"

supabase = create_client(url, key)


def scrape_github():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://github.com/ManthanS2003")
        page.wait_for_selector("span.p-nickname")

        username = page.locator("span.p-nickname").inner_text()

        name_element = page.locator("span.p-name")
        name = name_element.inner_text().strip() if name_element.count() > 0 else "Not Available"

        bio_element = page.locator("div.p-note")
        bio = bio_element.inner_text() if bio_element.count() > 0 else "No Bio"

        followers = page.locator("a[href$='followers'] span").first.inner_text()
        following = page.locator("a[href$='following'] span").first.inner_text()
        repos = page.locator("span.Counter").first.inner_text()

        data = {
            "username": username,
            "name": name,
            "bio": bio,
            "followers": int(followers.replace(",", "")),
            "following": int(following.replace(",", "")),
            "repositories": int(repos.replace(",", ""))
        }

        browser.close()
        return data


def save_to_supabase(data):
    response = supabase.table("github_profiles").insert(data).execute()
    print("✅ Data saved to Supabase")
    print(response)


if __name__ == "__main__":
    profile_data = scrape_github()

    print("Scraped Data:")
    print(profile_data)

    save_to_supabase(profile_data)