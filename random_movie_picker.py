import random
import tkinter
import requests
from bs4 import BeautifulSoup


def pick():
    movies = []
    for movie_info in all_movies:
        movie_name = movie_info.find("a").text
        movie_year = movie_info.find("span", class_="secondaryInfo").text
        # it doesn't look good with parenthesis
        movie_year = movie_year.replace("(", "").replace(")", "")
        movies.append((movie_name, movie_year))

    random_movie = random.choice(movies)
    return f"Name : {random_movie[0]}\nYear : {random_movie[1]}"


def re_run():
    # cover up the earlier label
    blank = tkinter.Label(root, text=f"{' '*100}\n{' '*100}", bg='black')
    blank.grid(column=0, row=1, padx=10, pady=10, columnspan=20)
    # generate new one
    label1 = tkinter.Label(root, text=pick(), bg='black', fg='white')
    label1.grid(column=0, row=1, padx=10, pady=10, columnspan=20)


def main():
    root.title("Choose It")
    root.geometry('327x200')
    button1 = tkinter.Button(root, text=" Generate ", command=re_run)
    button1.grid(column=0, row=0, padx=10, pady=10)
    root.mainloop()


if __name__ == '__main__':
    try:
        url = "https://www.imdb.com/chart/moviemeter?pf_rd_m=A2FGELUUNOQJNL&\
        pf_rd_p=cb6cf75a-1a51-49d1-af63-8202cfc3fb01&pf_rd_r=QKD7051N\
        5SWMFFW2V56N&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=moviemeter\
        &ref_=chtmvm_ql_2"
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'html.parser')
        all_movies = soup.find_all("td", class_="titleColumn")
    except:
        # Warning window
        root = tkinter.Tk()
        root.title("Choose It")
        warn_label = tkinter.Label(root,
                                   text="\n⚠ Check Your Internet Connection And Run Again ⚠\n",
                                   fg='red')
        warn_label.pack(anchor="center")
        root.mainloop()
        exit()
    root = tkinter.Tk()
    main()
