import requests as requests
from speedtesters import test_fast_com, test_broadbandspeedchecker_co_uk, test_speedtest_net
from plot_tests import plot_tests
import pandas as pd
from tkinter import *
from datetime import datetime

test_results = []
num_tests = 0
num_services = 0

root = Tk()
root.iconbitmap("icon.ico")
root.title("Internet Speed Checker")
root.geometry("1140x370+390+100")  # set starting size of window
root.minsize(1140, 370)  # width x height
root.config(bg="lightgrey")

# show services logos #
select_info = Label(root, text="Select internet speed test services:", bg="lightgrey")
select_info.config(font=('Courier',14))
select_info.grid(row=0, column=0, columnspan=12, padx=5, pady=5)

image_speedtest = PhotoImage(file="./img/speedtest.png")
img_speedtest = Label(root, image=image_speedtest)
img_speedtest.grid(row=1, column=0, columnspan=4, padx=10, pady=5)

image_fast = PhotoImage(file="./img/fast.png")
img_fast = Label(root, image=image_fast)
img_fast.grid(row=1, column=4, columnspan=4, padx=10, pady=5)

image_broad = PhotoImage(file="./img/broadband.png")
img_broad = Label(root, image=image_broad)
img_broad.grid(row=1, column=8, columnspan=4, padx=10, pady=5)

# selecting services #
on_image = PhotoImage(width=48, height=24)
off_image = PhotoImage(width=48, height=24)
on_image.put(("green",), to=(0, 0, 23,23))
off_image.put(("red",), to=(24, 0, 47, 23))

var_speedtest = IntVar(value=1)
cb_speedtest = Checkbutton(root, image=off_image, selectimage=on_image, indicatoron=False,
                     onvalue=1, offvalue=0, variable=var_speedtest)
cb_speedtest.grid(row=2, column=0, columnspan=4, padx=20, pady=5)

var_fast = IntVar(value=1)
cb_fast = Checkbutton(root, image=off_image, selectimage=on_image, indicatoron=False,
                     onvalue=1, offvalue=0, variable=var_fast)
cb_fast.grid(row=2, column=4, columnspan=4, padx=20, pady=5)

var_broad = IntVar(value=1)
cb_broad = Checkbutton(root, image=off_image, selectimage=on_image, indicatoron=False,
                     onvalue=1, offvalue=0, variable=var_broad)
cb_broad.grid(row=2, column=8, columnspan=4, padx=20, pady=5)


# number of repetitions #
var_num_of_cycles = IntVar()
var_num_of_cycles.set(3)  # default 3 repetitions
select_info = Label(root, text="Set the number of test repetitions:", bg="lightgrey")
select_info.config(font=('Courier',14))
select_info.grid(row=3, column=0, columnspan=12, padx=5, pady=20)
cycles_num =[("One",1,0),("Two",2,3), ("Three",3,6),("Four",4,9) ]
for button_text, val, col in cycles_num:
    Radiobutton(root, text=button_text, indicatoron = 0, variable=var_num_of_cycles, selectcolor="aquamarine",
                value=val, width=37).grid(row=4, column=col, columnspan=3)


def start_tests():
    global test_results
    global num_services
    global num_tests
    test_results = []

    terminal = Text(root, width=100, height=22)
    terminal.config(font=('Courier', 12))
    terminal.grid(row=6, column=0, columnspan=12)
    root.geometry("1140x850+390+100")

    ip=requests.get('https://api.ipify.org').content.decode('utf8')

    num_repetitions = var_num_of_cycles.get()
    num_services = var_speedtest.get() + var_fast.get() + var_broad.get()
    num_tests = num_repetitions * num_services

    terminal.insert(INSERT, f"Internet speed connection tests for IP {ip}."
                            f" {num_services} services * {num_repetitions} repetitions = {num_tests} tests total. \n\n")

    for repetition in range(num_repetitions):
        terminal.insert(INSERT, f"Repetition {repetition+1} of {num_repetitions}:\n")
        rep_result = []
        if var_speedtest.get()==1:
            result = test_speedtest_net()
            rep_result.append(result)
            test_results.append(result)
        if var_fast.get() == 1:
            result = test_fast_com()
            rep_result.append(result)
            test_results.append(result)
        if var_broad.get() == 1:
            result = test_broadbandspeedchecker_co_uk()
            rep_result.append(result)
            test_results.append(result)
        df_cycle_result = pd.DataFrame(rep_result)
        df_cycle_result.rename(columns={'service_name': 'service name', 'ping': 'ping, ms',
                                        'upload_speed': 'upload, Mb/s', 'download_speed': 'download, Mb/s',
                                        'duration': 'duration, s' ,'test_date': 'date', 'test_time': 'time'},inplace = True)
        terminal.insert(INSERT, df_cycle_result.to_string(index=False))
        terminal.insert(INSERT, "\n\n")

    df = pd.DataFrame(test_results)
    now=datetime.now()
    results_filename='./results/'+now.strftime("%Y%m%d-%H%M%S")+".csv"
    df.to_csv(results_filename)
    print (f"Results has been saved to saved to {results_filename}")
    terminal.insert(INSERT, f"\nResults are saved to {results_filename}")


def analyze_result():
    print (num_services)
    plot_tests(root,test_results, num_tests, num_services)


Button(root, text="Start test", command=start_tests, fg = "red", font = "Verdana 14",
                bd = 2, bg = "light blue", relief = "groove").grid(row=5, column=0, columnspan=12, pady=20)

Button(root, text="Analyze", command=analyze_result, fg = "green", font = "Verdana 14",
                bd = 2, bg = "light blue", relief = "groove").grid(row=7, column=0, columnspan=12, pady=20)

root.mainloop()
