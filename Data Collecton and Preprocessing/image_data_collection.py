from bing_image_downloader import downloader
import http.client as httplib
def download(apa_yang_mau_didownload, limit, output_dir='indonesian_food'):
    try:
        downloader.download(apa_yang_mau_didownload, limit=limit, output_dir=output_dir, adult_filter_off=True)
    except httplib.IncompleteRead as e:
        print("ada yang error:", str(e))


download('ayam geprek', 200)
download('mie ayam', 200)
download('sayur asem', 200)
download('soto ayam', 200)
