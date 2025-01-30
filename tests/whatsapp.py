from fixtures import *
from modules import common, locators
import time

def test_send_messages(web_page, config_data):
    web_page.goto("https://web.whatsapp.com")
    data = ["3434343434"]
    message = """
💥 Offer Alert by Catalyst Programmers! 💥
💻 New Batch Starting: 1st February 2025
🎯 Course Fee: Only ₹499!

🚀 Why Join Catalyst Programmers?
✔️ Learn from industry-leading experts.
✔️ Hands-on projects to enhance your skills.
✔️ Affordable and beginner-friendly.
✔️ Get ready for a bright career in tech!

🌐 Enroll Now:
👉 Official Website: www.catalystprogrammers.in
👉 Registration Form: https://docs.google.com/forms/d/e/1FAIpQLSfmh94p-g4PExIzPYQtWz1L5BwURkfUew_OC66XzLpajZGB-g/viewform

📞 Contact Us: +91-8503967987

⚡ Limited Seats Available! Don't miss this chance to kickstart your programming journey with Catalyst Programmers.

✨ Stay Connected with Catalyst Programmers ✨
👉 Instagram: https://www.instagram.com/catalystprogrammers
👉 YouTube: https://youtube.com/@catalystprogrammers

💻 Like, follow, and subscribe to stay updated and never miss exciting offers! 🚀
"""
    breakpoint()
    def send_msg(mobile_number, image_path = ""):
        try:
            common.click_or_validate_element(web_page, '//span[@data-icon="new-chat-outline"]', method="locator", take_screenshot=False)
            time.sleep(3)
            common.click_or_validate_element(web_page, '//div[@contenteditable="true"]', method="locator", take_screenshot=False, select_element=0, fill=mobile_number)
            time.sleep(3)
            try:
                common.click_or_validate_element(web_page, '//span[@class="x1iyjqo2 x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft x13faqbe _ao3e"]', method="locator", take_screenshot=False)
                time.sleep(3)
            except:
                common.click_or_validate_element(web_page, '//span[@class="x1iyjqo2 x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft x13faqbe _ao3e"]', method="locator", take_screenshot=False, select_element=0)
                time.sleep(3)
            common.click_or_validate_element(web_page, '//span[@data-icon="plus"]', method="locator", take_screenshot=False)
            time.sleep(3)
            with web_page.expect_file_chooser() as fc_info:
                common.click_or_validate_element(web_page, '//div[@class="x1c4vz4f xs83m0k xdl72j9 x1g77sc7 x78zum5 xozqiw3 x1oa3qoh x12fk4p8 xeuugli x2lwn1j x1nhvcw1 x1q0g3np x6s0dn4 x1ypdohk x1vqgdyp x1i64zmx x1gja9t"]', method="locator", take_screenshot=False, select_element=1)
                time.sleep(3)
            file_chooser = fc_info.value
            time.sleep(3)
            file_chooser.set_files(image_path)
            time.sleep(3)
            common.click_or_validate_element(web_page, '//div[@contenteditable="true"]', method="locator", take_screenshot=False, select_element=0, fill=message)
            time.sleep(3)
            common.click_or_validate_element(web_page, '//span[@data-icon="send"]', method="locator", take_screenshot=False)
            time.sleep(3)
        except:
            web_page.reload()
            time.sleep(10)
            common.add_to_logs(f"Failed to find {number} On What's APP.")
    for number in data:
        send_msg(number, config_data.get("image_file_path"))
    breakpoint()
