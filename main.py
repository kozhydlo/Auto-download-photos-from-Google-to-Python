from icrawler.builtin import GoogleImageCrawler

def google_img_downloader():
    filters = dict(
        type='photo',
        color='blackandwhite'
        # size='lagre'
        # license='noncommercial, commercial',
        # date=(2020, 1, 1), (2022, 5, 14))
    )
    
    crawler = GoogleImageCrawler(storage={'root_dir': './img'})
    # crawler.crawl(keyword='mr.robot', max_num=5)
    # crawler.crawl(keyword='code', max_num=5, min_size=(1000, 1000,), overwrite=True)
    # crawler.crawl(
    #     keyword='Ukraine Lviv', 
    #     max_num=5, 
    #     min_size=(1000, 1000,), 
    #     overwrite=True,
    #     filters=filters,
    #     file_idx_offset='auto'
    # )
    crawler.crawl(
        keyword='Ukraine Lviv', 
        max_num=5, 
        min_size=(1000, 1000,), 
        overwrite=True,
        filters=filters,
        file_idx_offset='auto'
    )

def main():
    google_img_downloader().download

if __name__ == '__main__':
    main()