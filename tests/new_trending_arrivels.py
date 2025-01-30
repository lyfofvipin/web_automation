from fixtures import *
from modules import common, locators
import requests


def test_myntra(web_page, config_data):
    web_page.goto("https://www.myntra.com/women-kurtas-kurtis-suits?f=Country%20of%20Origin%3AIndia&sort=new")
    new_tab = common.click_or_validate_element(web_page, locators.all_myntra_items, method="locator", select_element=0, new_tab=True)
    new_tab.value.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    import pdb;pdb.set_trace()
    images = common.click_or_validate_element(new_tab.value, locators.all_myntra_images, method="locator", click=False)
    for image in range(images.count()):
        common.add_to_logs(f"working with image {image}")
        html_content = images.nth(image).inner_html()
        common.add_to_logs(html_content)
        image_url = html_content.split("&quot;")[1]
        image_url = image_url.replace("h_720,q_90,w_540", "h_1440,q_90,w_1080")
        common.add_to_logs(f"Image url : {image_url}")
        image_content = requests.get(image_url)
        with open(f"{common.myntra_pics}{image}.png", "wb") as image_file:
            image_file.write(image_content.content)

# def test_savana(web_page, config_data):
#     web_page.goto("https://www.savana.com/category/new-in/new-in-dresses-1102?0=0")
#     common.click_or_validate_element(web_page, locators.all_savana_items, method="locator", select_element=0)
#     web_page.get_by_label("close").locator("path").click()
#     web_page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
#     images = common.click_or_validate_element(web_page, locators.all_savana_images, method="locator", click=False)
#     for image in range(images.count()):
#         common.add_to_logs(f"working with image {image}")
#         html_content = images.nth(image).inner_html()
#         common.add_to_logs(html_content)
#         image_url = html_content.split("\"")[3]
#         common.add_to_logs(f"Image url : {image_url}")
#         image_content = requests.get(image_url)
#         with open(f"{common.savana_pics}{image}.png", "wb") as image_file:
#             image_file.write(image_content.content)

# def test_newmw_asia(web_page, config_data):
#     web_page.goto("https://newme.asia/womens-collection/mini/?orderby=menu_order&p=1")
#     common.click_or_validate_element(web_page, locators.all_new_asia_items, method="locator", select_element=2)
#     images = common.click_or_validate_element(web_page, locators.all_new_asia_images, method="locator", click=False)
#     for image in range(images.count()):
#         common.add_to_logs(f"working with image {image}")
#         html_content = images.nth(image).inner_html()
#         breakpoint()
#         common.add_to_logs(html_content)
#         image_url = html_content.split("\"")[3]
#         common.add_to_logs(f"Image url : {image_url}")
#         image_content = requests.get(image_url)
#         with open(f"{common.new_asia_pics}{image}.png", "wb") as image_file:
#             image_file.write(image_content.content)

def test_make_video(config_data):
    from moviepy.editor import ImageSequenceClip
    directory_path = common.savana_pics
    directory_path = common.myntra_pics

    clip = ImageSequenceClip(directory_path, fps=1)  # Set FPS to 1 for a 1-second gap
    # Write the clip to a video file
    clip.write_videofile('/home/vipikuma/Downloads/output.mp4')
