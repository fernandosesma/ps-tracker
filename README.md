# PlayStation 5 Tracker [v1.0.2]

### **Motivation**
Obtaining a PlayStation 5 has become a three-way battle between botters, scalpers, and legitimate buyers. This program uses web scraping to automate the process of refreshing storefront pages to check for new PS5 stock. Currently, the program checks Amazon, Best Buy, Target, and PlayStation Direct. The code uses the *time*, *webbrowser*, *selenium*, and *plyer* packages.

The program does not seek to automate the process of *checking out* on the storefront. It only seeks to resolve the issue of imperfect notification channels (i.e. NowInStock, Twitter). The author sees the practice of total automation in purchasing to be unethical (as most people who engage seek to hoard and/or scalp supply).

### **Methodology**
Read on to learn more about how the program works. Currently using *ChromeDriver 99.0.4844.51*. **Note: The program will only work if you're using Chrome version 99. I will continue to update the program for future versions of Chrome.**
* The user must enter the absolute path of wherever *chromedriver.exe* is stored on their local machine. The user will be prompted to do so at the beginning of program execution.
* `statusInit()` checks each storefront for the current (or what will be *old*) status on stock. *Selenium* will open the Chrome browser and seek the HTML container noting stock status via XPath for each storefront. *Important Note:* The third index corresponds to the PlayStation Direct storefront, but uses *Selenium's* `find_elements` *(plural)* method instead of the `find_element` *(singular)* method. I could not accurately find the proper element with the singular method. This is evident in the rest of the code and will be fixed in later builds.
* `windowInit()` will initialize where the main loop runs. All storefront pages open in the same window in separate tabs then return to the first tab to begin checking.
* `storeNotify()` triggers a Windows notification when a store has new stock.
* **MAIN LOOP**: Similar to the other methods, the program retrieves whether or not each storefront has stock by checking the corresponding HTML container via XPath (checking every 20 seconds with the *time* package). The *new* status is then compared to what was initialized at the beginning of the program (*old* status). When the HTML element has changed, this means the storefront has new stock and thus the `while` loop will trigger the `else` condition. Then (from the *plyer* package) the user will receive a Windows notification that the corresponding storefront has new stock.

## Number of PS5s bought: **0** (gotta start somewhere)