from flask import Flask, render_template, request
import requests
import os
import concurrent.futures
import asyncio
from PIL import Image
import argparse
import time

app = Flask(__name__)

def download_image(url):
    start_time = time.time()
    response = requests.get(url, stream=True)
    image_name = url.split('/')[-1].split('@')[0]  # Используем только имя файла

    with open(image_name, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

    end_time = time.time()
    download_time = end_time - start_time

    print(f"Downloaded {image_name} in {download_time:.2f} seconds")

    return image_name, download_time

def determine_extension(image_path):
    image = Image.open(image_path)
    format_extension = Image.registered_extensions().get(image.format, 'jpg')
    return format_extension

async def rename_image(image_name):
    format_extension = determine_extension(image_name)
    new_image_name = f'{os.path.splitext(image_name)[0]}.{format_extension}'
    os.rename(image_name, new_image_name)
    return new_image_name

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    urls = request.form.getlist('urls')
    saved_image_names = []
    download_times = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(download_image, url) for url in urls]
        for future in concurrent.futures.as_completed(futures):
            image_name, download_time = future.result()
            saved_image_names.append(image_name)
            download_times.append(download_time)

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(asyncio.gather(*[rename_image(image_name) for image_name in saved_image_names]))

    total_time = sum(download_times)
    print(f"Total time: {total_time:.2f} seconds")

    return "Images downloaded and processed successfully!"

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download and process images from URLs')
    parser.add_argument('urls', nargs='+', help='List of URLs to download images from')

    args = parser.parse_args()

    urls = args.urls

    if not os.path.exists('images'):
        os.makedirs('images')

    if urls:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(download_image, url) for url in urls]
            for future in concurrent.futures.as_completed(futures):
                image_name, _ = future.result()
                saved_image_names.append(image_name)

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(asyncio.gather(*[rename_image(image_name) for image_name in saved_image_names]))

        print("Images downloaded and processed successfully!")
    else:
        app.run(debug=True)
