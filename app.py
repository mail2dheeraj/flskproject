from flask import Flask,url_for,render_template,jsonify,request,send_from_directory,redirect;
import logging as lg;
import loggin as domain;
import os;
import jinja2;
from flask_socketio import SocketIO;
from flask_sock import Sock
from mongodbsetup import createMongoConnectionObject;
from bs4 import BeautifulSoup as bs;
from selenium import webdriver
from selenium.webdriver.common import keys
import requests as rs
from selenium.webdriver.chrome.options import Options
import pandas as pd;
import time as te;
import plotly.offline as po;
import plotly.express as px;
import plotly.graph_objects as go;
# import scrapy as scrap;
crome_driver_path = 'E:/inuron/videos/scraping and seaborn/chromedriver.exe';

chrome_options = Options()
chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    # chrome_options.binary_location = CHROME_PATH




# driver.get('https://www.espncricinfo.com/')
# zz=driver.find_element_by_xpath("//a[@data-hover='Teams']")

# zz.click();
# az=driver.find_element_by_xpath("//*[@id='navbarSupportedContent']/ul[2]/div/li")

# az.click()
# pp=driver.find_element_by_xpath("//*[@id='navbarSupportedContent']/ul[2]/div/div/div/form/input")
# pp.send_keys('Sachin');
# pp.send_keys(keys.ENTER);
# zz=driver.find_element_by_xpath("//*[@id='navbarSupportedContent']/ul[2]/div/div/div/form/button")

# zz.click();
print('gggggggggggggggggggggggggggggggggggggggggggggggggggg')
# print(driver.page_source)
# bs=BeautifulSoup(driver.page_source,'html.parser')
# ele=bs.xpath("//*[@id='navbarSupportedContent']/ul[2]/div/div/div/form/input")
# print(bs)
# driver.close()
# zz=rs.get('https://www.espncricinfo.com/')
# for i in :
    # print(i)
# kk=[i for i in zz]
# print(kk)    
loger=domain.loggin()
doimanFile=loger.writingInfile();
domainConsole=loger.writeInConsolo();

db_connection=createMongoConnectionObject();
main_db=db_connection.sendMongoConnection()
domainConsole.info('mongo connection seccused');
print(main_db)

######################
vsTeam='#main-container > div:nth-child(1) > div > div.container > div > div.playerpage-content > div.card.stats_mobile-negative-margin.player-stats-containter-mobile-bp > div:nth-child(3) > div';
inHostCountry = '#main-container > div:nth-child(1) > div > div.container > div > div.playerpage-content > div.card.stats_mobile-negative-margin.player-stats-containter-mobile-bp > div:nth-child(4) > div'
inContinent = '#main-container > div:nth-child(1) > div > div.container > div > div.playerpage-content > div.card.stats_mobile-negative-margin.player-stats-containter-mobile-bp > div:nth-child(5) > div'
homeVsAway = '#main-container > div:nth-child(1) > div > div.container > div > div.playerpage-content > div.card.stats_mobile-negative-margin.player-stats-containter-mobile-bp > div:nth-child(6) > div'
byEar= '#main-container > div:nth-child(1) > div > div.container > div > div.playerpage-content > div.card.stats_mobile-negative-margin.player-stats-containter-mobile-bp > div:nth-child(7) > div'
    
# try:
#     zk=main_db['sub']
#     collections1=zk['super']
#     collections1.insert_one({'name':'happy'})
#     print(main_db.list_database_names())
#     print('inserted')
# except Exception as e:
#     domainConsole.error('Error inserting');
#     doimanFile.error(f'Error inserting2')
# template_dir = os.path.join(template_dir,'\practice\flaskProject\template')
# domain.logger.error(template_dir)
app = Flask(__name__, template_folder ='views', static_folder='stastic');

# app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app)
# sock = Sock(app)

# my_loader = jinja2.ChoiceLoader([
#         app.jinja_loader,
#         jinja2.FileSystemLoader(['/flaskProject/views']),
#     ])


# app.jinja_loader = my_loader
@app.route('/uploadimg',methods=["GET"]) 
def homePage():
        # domain.view_log.info('This is a warning message')  
        # domain.logger.error('This is an error message')   
        # domain.logger.critical('Dheeraj')
        
        domainConsole.info('This is a warning message')  
        domainConsole.error('This is an error message')   
        doimanFile.critical('Dheeraj File')
        
        # logg.error('hii')
        # ap0=os.path.join(template_dir,'homePage','home.html',template_folder='folder1')
        # return render_template('homePage\home.html',template_folder=template_dir);
        replies = {'Jack':'Cool post',
			   'Jane':'+1',
			   'Erika':'Most definitely',
			   'Bob':'wow',
			   'Carl':'amazing!'};
         
        # return send_from_directory('views','homePage/home.html')  
        return render_template('homePage/home2.html',replies=replies)
    # views\homePage\home.html
    
@app.route('/resiveScrapingUrl',methods=['POST'])
def geturl():
    print(request.form['scrapingUrl']);
    driver = webdriver.Chrome(executable_path=crome_driver_path)
    driver.get(request.form['scrapingUrl'])
    
    # selectedElement=driver.find_element_by_css_selector('#main-container > div:nth-child(1) > div > div.container > div > div.playerpage-content > div.card.stats_mobile-negative-margin.player-stats-containter-mobile-bp > div:nth-child(3) > div')
    selectorDropdown=driver.find_element_by_css_selector('#main-container > div:nth-child(1) > div > div.container > div > div.playerpage-content > div.card.stats_mobile-negative-margin.player-stats-containter-mobile-bp > div.player_stats-header.d-flex.justify-content-between.align-items-center > div > div > div:nth-child(1) > button')
    selectorDropdown.click()
    if (request.form['matchFormat'] == 'Test') :
        try :
            
            
            selectfiefd=driver.find_element_by_css_selector('#main-container > div:nth-child(1) > div > div.container > div > div.playerpage-content > div.card.stats_mobile-negative-margin.player-stats-containter-mobile-bp > div.player_stats-header.d-flex.justify-content-between.align-items-center > div > div > div:nth-child(1) > div > div > ul > li.ci-dd__selected-option')
            selectfiefd.click()
        except Exception as e:
            domainConsole.error(e)   
            doimanFile.critical(e)
            
    if (request.form['matchFormat'] == 'odi') :
        try :
            
            selectfiefd=driver.find_element_by_css_selector('#main-container > div:nth-child(1) > div > div.container > div > div.playerpage-content > div.card.stats_mobile-negative-margin.player-stats-containter-mobile-bp > div.player_stats-header.d-flex.justify-content-between.align-items-center > div > div > div:nth-child(1) > div > div > ul > li:nth-child(2)')
            selectfiefd.click()    
        except Exception as e :
            domainConsole.error(e)   
            doimanFile.critical(e)
        
    if (request.form['matchFormat'] == 'Test') :
        try:
            
            
            selectfiefd=driver.find_element_by_css_selector('#main-container > div:nth-child(1) > div > div.container > div > div.playerpage-content > div.card.stats_mobile-negative-margin.player-stats-containter-mobile-bp > div.player_stats-header.d-flex.justify-content-between.align-items-center > div > div > div:nth-child(1) > div > div > ul > li:nth-child(3)')
            selectfiefd.click()
        except Exception as e :
            domainConsole.error(e)   
            doimanFile.critical(e)
    vs=''        
    if (request.form['vs'] == 'vs Team') :
        vs=vsTeam;
    if (request.form['vs'] == 'In Host Country') :
        vs=inHostCountry;    
    if (request.form['vs'] == 'in Continent') :
        vs=inContinent;            
    if (request.form['vs'] == 'Home vs Away') :
        vs=homeVsAway;          
    if (request.form['vs'] == 'By Year') :
        vs=byEar;              
        
    te.sleep(5)
    selectedElement=driver.find_element_by_css_selector(vs)
    
    table=selectedElement.get_attribute('innerHTML');
    soupobj=bs(table,'html.parser')
    
    allLinksinTable = soupobj.find_all('a')
    
    
    dataframe=pd.read_html(table)
    fig0=[];
    
    for i in list(dataframe[0].index):
        fig0.append(go.Scatter(x=[dataframe[0]['Span'][i]],y=[dataframe[0]['Runs'][i]],mode='markers',name=str(dataframe[0]['Title'][i]),hovertemplate=f"HS:{[dataframe[0]['HS'][i]]}<br>AVG:{[dataframe[0]['Avg'][i]]}"))
   
    fig0.append(go.Scatter(x=dataframe[0]['Span'],y=dataframe[0]['Runs'],mode="lines"))
    fig=go.Figure(data=fig0)
    po.plot(fig,filename="views/homePage/first_figure.html",auto_open=False)
    te.sleep(5)
    driver.close()
    # return redirect(url_for('http://localhost:8000/graphview'))
    return {'uri':'/graphview'}

@app.route('/graphview')
def showGraph():
    return render_template('homePage/first_figure.html')
        
@app.route('/',methods=['GET'])
def vedioPage():
    try :
        return render_template('homePage/home.html')               
    except Exception :
        
        domainConsole.error('video page rendring error')   
        doimanFile.critical('video page rendring error')
    
# @socketio.on('connecteduser')
# def showConnectedMsg(data):
#     print(data)    

    # while True:
    #     data = ws.receive()
    #     ws.send(data)
       
if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True);    
    # socketio.run(app,host="localhost", port=3030, debug=True)
    # websockets.serve('hello', "localhost", 8765);    
    