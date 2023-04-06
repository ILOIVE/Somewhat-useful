import youtube_dl #youtube_dl module. used for downloading youtube vidoes in various formats


url = [] #empty url array. An array is used in order to store multiple urls 


#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------

#download_video function. information dictionary (presented as 'info_dict') contains what format and by what name the file should be downloaded

def download_video(url): 
    info_dict = {
        'format' : f'{quality}',
        'outtmpl' : '%(title)s.%(ext)s'
    }
    with youtube_dl.YoutubeDL(info_dict) as ydl :
        while True : 
            try:
                for i in url:
                    ydl.download([i])
                    break
            except : 
                print("Can't download this file. Try again later or try another URL.")
                main()

#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------

#download_quality function. Users can select the desierd quality and format to download their links. 

def selceted_quality():
    global quality
    quality = ''
    while True:
        quality_check = input("Please choose your quality (high / low) : ")
        format_check = input("Please enter the format (Audio / Video) : ")
        
        if quality_check.lower() == "high" :

            if format_check.lower() == "audio":
                quality = "bestaudio/best"
                return quality

            elif format_check.lower() == "video":
                quality = "bestvideo/best"
                return quality
        
        elif quality_check.lower() == "low" :

            if format_check.lower() == "audio":
                quality = "worstaduio/worst"
                return quality
            
            elif format_check.lower == "vidoe":
                quality = "worstvideo/worst"
                return quality
                
        else : 
            print("Please enter valid options.")

#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------

def main():
    print("Please note that some qualiteis and formats might be unavailable.")

    while True:
        queue = input("Please enter URL : ")
        url.append(queue)
        more_downloads = input("would you like to download another url? (yes/no) : ")
        if more_downloads.lower() != "yes" : 
                break 
         
    selceted_quality()
    download_video(url)
    
#--------------------------------------------------------------------------------------------------

if __name__ == "__main__" : 
   print("Welcome to the youtube downloader!")
   main()
   
    