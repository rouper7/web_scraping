#Use Jupyter to make the code work and change the file extension to .ipynb
# %%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# %%
driver=webdriver.Firefox()
driver.get("https://www.youtube.com/")


# %%

wait=WebDriverWait(driver,50)
wait.until(EC.presence_of_element_located((By.XPATH,"//button[contains(@title,'Pesquisar')]")))
search=driver.find_element(By.NAME,"search_query")

button=driver.find_element(By.XPATH,"//button[contains(@title,'Pesquisar')]")
search.clear()
ActionChains(driver).click(search).send_keys("teste").perform()
ActionChains(driver).click(button).perform()




# %%
import pymysql
import time



try:
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="1234",
        database="PYTHON"  
    )
    print(" a coneção deu certo")
except pymysql.MySQLError as e:
    print(f"a conecao deu erro porque: {e}")

    raise SystemExit


try:
    time.sleep(10)

    wait.until(EC.presence_of_element_located((By.ID, "video-title")))
    search=driver.find_element(By.NAME,"search_query")
    video_titles=[]

    for i in range(5):
        ActionChains(driver).scroll_by_amount(0,10000).perform()
        video_elements = driver.find_elements(By.ID, "video-title")
        for video in video_elements:
            video_titles.append(video)
        
        time.sleep(5)


    website_title=driver.title
    cursor = db.cursor()




    for title in video_titles:
        print(title.text)
        
        sql = f"INSERT INTO informacoes VALUES (NULL,'{website_title}','{title.text}');"
        cursor.execute(sql)
        db.commit()




    print("Conexão estabelecida com sucesso!")


    cursor.close()
    db.close()
except Exception as e:
    print(f"ocorreu um erro:{e}")



