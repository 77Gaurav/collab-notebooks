url = "https://string-theory-original-videos.s3.ap-south-1.amazonaws.com/originals/f6d138d6-9202-4fea-8e43-fcaa4090d04e/4c1fd60b-2d18-46ab-873d-645325603f19.mp4?response-content-disposition=inline&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCmFwLXNvdXRoLTEiRzBFAiEA0KcDATJ%2FjrbJ6l0%2BKn4JmLd7HWKcU5IwuYmvpgXVpQUCIGzpr%2BUSOIO2N7I6UT8nV6M1BZ6wfSbHUJLax0qwnhw6KsgECGQQABoMMjEwODU1NDgyNTM1IgyLTfQqkv3wwwW8sZIqpQQ73mR6X57Qlkkig9k4PdA1R7YiWDzTlur%2BrZTBtjGbOXC6EjY%2Fqmxa0mZFB0GPzI%2FlRNgkX0KxG2G98JYYUG7ZsxCC6hi7ggmzfZJ6wSDR6GB03TdIwELUbHmNRIkIj8DVL5SHKr2qgj89a%2FF9Psz%2FHhWrGntwGrMlqYOtBeZL7WdqIhZzOnO1Jdpq2lqtMchCdYCmnBQw%2FF38Gqjsvm8yRsEu53rcbw9HWOJTgfAnLF3MwUitkdO1yauAC5%2Fh4BSaKHfTF5OohXfMFT7zyHYvlnU50D4EfIfDJvNGnsVocGBHRPdYOZmc40LnnX9iGw9scZdonr3Di2ejo7gz6LFSyB3bfr74ztWqbcnlCJWh40VgvQtqBSxV%2BGGms%2BAgmqq%2FfxSAeFZxs9iuUojlu7JCJdFDzSltbFo2%2FJo2iaPYphkHzhM%2BxpbePwxhHdagUxgHBNKudQyTmEZTeeaJlM1xaOHWun5Glvrfmtm%2FW6zhlg1Z0xwfeOaW7UftMz5OFrrsx0PxSbOcfKz0t80QZygPhzdUZ3FHsZQLQboECBCRUCLBDMkSZeTj9a%2BNiDCrptPPGGqBL16xT43CmWqljFTXbj9Y3SjQ%2BqdObtr8c%2BjdeGUBsXHfSJE6PrSiya4AAWhzerQ4i8DEkWVpb6FMt0HiQZI%2BIJy1%2F0CL4XKd%2BzrBfJdkevD7CiP%2BrbS9qz38zDrxdL93cDO5FEdCcOeAhHBm1VdgqeIwubvj1gY66wJe90QOYVVw3P0rYWL7%2B6%2B9g1GcG2p0b3cm8fw8iLrroaFVySzAXIZzTyeMqk4oNYHk%2FOqI1AD0XQEr3%2FmfeRlglnS1X6jdGruVz%2BCDPyrowtu7QVrx9SJ1fyYm4spE2%2FdJRPMIdAefExoe65eQ20l9kRRuzQjObAy9N0xSbGY27eR%2F9g6Wp5TJPLNBZKy%2FgKSPY0HQHfQ8uTAgOGgh13N6ECxkk9dYF7uV76f3jHBpmEJGvcx5l1sQ1r7UNaSbXh45A0VPoBCJ1MgoeUqhIYmeMvNVdFpro39iRPYhbqBEnQL3xq4bCqoMJTTNUjQFyV8uAcHD8XGUSwJP3BySyrqXOcYY3lsi730VClO9wHzBfCqvy0GuigddyYf9CW9E1CdgJ63I2f2VhsA3nxw6BpT6oj4UuVC52m6ljzR0pWJ9%2BBckbVjJgu3t121ATBmZnjwiIVpijmEjbLHUMzS3JwmSfzDQdIA2GT7FF4c%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIATCF7XKST74T3ODW2%2F20261021%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Date=20261021T185442Z&X-Amz-Expires=1200&X-Amz-SignedHeaders=host&X-Amz-Signature=a2559ee5a7985babb71b15d6f322eb6ec020b63422ea002e41a993645c6ff61e"


import requests

def download_video(presigned_url: str, output_path: str) -> None:
    with requests.get(presigned_url, stream=True, timeout=(10, 60)) as response:
        response.raise_for_status()

        with open(output_path, "wb") as video:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    video.write(chunk)

    print(f"Downloaded: {output_path}")


if __name__ == "__main__":
    #url = input("Presigned S3 URL: ").strip()
    download_video(url, "video.mp4")