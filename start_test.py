from click import confirm
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from settings import settings
from test_cases import test_cases as cases
import time


# testing configurations
MAX_WAIT_TIME = 40
SPEED = 0.5


# adding metamask extension
chop = webdriver.ChromeOptions()
chop.add_extension(settings.METAMASK_PATH)

# Creation of webdriver whit metamask extension
driver = webdriver.Chrome(settings.DRIVER_PATH, chrome_options=chop)
driver.maximize_window()
driver.get(settings.GALLERY_URL)

# global Elements
gallery_search_bar = None
button_open_filters = None
button_open_filters = None
artist_dropdown = None
cards_dropdown = None
sort_dropdown = None
view_dropdown = None


# it_exception = True
# while it_exception:
#   try:
#     gallery_search_bar = driver.find_element_by_id("inputSearch")
#     button_open_filters = driver.find_element_by_class_name("css-fponm9")
#     time.sleep(1)
#     button_open_filters.click()
#     artist_dropdown = Select(driver.find_element_by_id("filterArtist"))
#     cards_dropdown = Select(driver.find_element_by_id("filterCards"))
#     sort_dropdown = driver.find_element_by_id("filterSortBy")
#     view_dropdown = driver.find_element_by_id("filterView")

#     it_exception = False
#   except:
#     it_exception = True
#     time.sleep(0.1)
    


# driver.switch_to_window
# mtmsk_get_started = driver.find_element_by_class_name("first-time-flow__button")


def run_test():
  initialize()
  exchange_crypto(0.00002)

  # test_case_1()
  # sys.exit(0)

def initialize():
  login_metamask()
  # ALTERNATIVE METHODfrancisco.tun@avocadoblock.com

  driver.switch_to.window(driver.window_handles[0])
  time.sleep(1)
  driver.get('https://cryptoloteria.mx')
  connect_wallet()
  time.sleep(2)
  driver.get(settings.HOST)
  time.sleep(1)
  connect_wallet_2()
  time.sleep(1)

def exchange_crypto(amount):
  driver.get(settings.GALLERY_URL)
  print("WAITING 5 SECONDS FOR GALLERY TO LOAD")
  time.sleep(7)

  it_exception = True
  while it_exception:
    try:
      button_open_filters = Select(driver.find_element_by_class_name("css-1ilbin4"))
      button_open_filters.select_by_visible_text("Unlocked")
      it_exception = False
    except:
      it_exception = True
      time.sleep(0.1)

  time.sleep(7)
  it_exception = True
  while it_exception:
    try:
      gallery_search_bar = driver.find_element_by_class_name("MuiInputBase-inputTypeSearch")
      search_in_bar(gallery_search_bar, cases.NFT_STRINGS['ERICK'][0])
      it_exception = False
    except:
      it_exception = True
      time.sleep(0.1)

  it_exception = True
  while it_exception:
    try:
      las_jaras_card = driver.find_elements_by_class_name("MuiCardMedia-media")
      las_jaras_card[0].click()
      it_exception = False
      time.sleep(SPEED)
    except:
      it_exception = True
      time.sleep(0.1)


  it_exception = True
  while it_exception:
    try:
      exchange_dropdown = Select(driver.find_element_by_class_name("css-1ogpdw0"))
      select_item_from_dropdown(exchange_dropdown, 2)
      it_exception = False
      time.sleep(SPEED)
    except:
      it_exception = True
      time.sleep(0.1)

  it_exception = True
  while it_exception:
    try:
      input_amount = driver.find_elements_by_class_name("MuiInput-input")
      fill_input(input_amount[2], amount)
      it_exception = False
      time.sleep(SPEED)
    except:
      print("ERROR FILLING INPUT")
      it_exception = True
      time.sleep(0.1)

  it_exception = True
  while it_exception:
    try:
      chnge_matic = driver.find_element_by_class_name("css-k0sj4s")
      chnge_matic.click()
      it_exception = False
      time.sleep(SPEED)
    except:
      print("ERROR CLICKING OFFER")
      it_exception = True
      time.sleep(0.1)



  it_exception = True
  duration = 0
  while it_exception:
    try:
      chnge_matic = driver.find_element_by_class_name("css-pisl68")
      chnge_matic.click()
      it_exception = False
      time.sleep(SPEED)
    except:
      duration += 0.1
      print(duration)
      if duration > 20:
        it_exception = False
        print("Chnahge matic not found\nTrying to sign...")
      else:
        print("ERROR ON CHANGE MATIC")
        it_exception = True
        time.sleep(0.1)


  it_exception = True
  while it_exception:
    try:
      sign_wmatic = driver.find_element_by_class_name("css-k0sj4s")
      sign_wmatic.click()
      it_exception = False
      time.sleep(SPEED)
    except:
      print("TEST_ERROR ON CHANGE MATIC")
      it_exception = True
      time.sleep(0.1)
    
  
  time.sleep(5)
  driver.switch_to.window(driver.window_handles[0])


  # it_exception = True
  # while it_exception:
  #   try:
  #     confirm_btn = driver.find_element_by_class_name("btn-primary")
  #     confirm_btn.click()
  #     it_exception = False
  #     time.sleep(SPEED)
  #   except:
  #     print("TEST_ERROR ON CONFIRM")
  #     it_exception = True
  #     time.sleep(0.1)




def login_metamask():
  driver.switch_to.window(driver.window_handles[0])
  it_exception = True
  while it_exception:
    try:
      mtmsk_get_started = driver.find_element_by_class_name("first-time-flow__button")
      mtmsk_get_started.click()
      it_exception = False
    except:
      it_exception = True
      time.sleep(0.1)
  it_exception = True
  while it_exception:
    try:
      mtmask_import_wallet = driver.find_elements_by_class_name("first-time-flow__button")
      mtmask_import_wallet[0].click()
      it_exception = False
    except:
      it_exception = True
      time.sleep(0.1)
  it_exception = True
  while it_exception:
    try:
      mtmsk_get_iagree = driver.find_elements_by_class_name("page-container__footer-button")
      mtmsk_get_iagree[1].click()
      it_exception = False
    except:
      it_exception = True
      time.sleep(0.1)
  # fill form
  it_exception = True
  while it_exception:
    try:
      mtmsk_form_input = driver.find_elements_by_class_name("MuiInput-input")
      mtmsk_check = driver.find_elements_by_class_name("first-time-flow__terms")
      mtmsk_import = driver.find_elements_by_class_name("first-time-flow__button")
      fill_input(mtmsk_form_input[0], settings.METAMASK_MNEMONIC)
      fill_input(mtmsk_form_input[1], settings.METAMASK_PASS)
      fill_input(mtmsk_form_input[2], settings.METAMASK_PASS)
      mtmsk_check[0].click()
      mtmsk_import[0].click()
      it_exception = False
    except:
      it_exception = True
      time.sleep(0.1)
  # All done
  it_exception = True
  while it_exception:
    try:
      mtmsk_all_done = driver.find_element_by_class_name("first-time-flow__button")
      mtmsk_all_done.click()
      driver.close()
      it_exception = False
    except:
      it_exception = True
      time.sleep(0.1)


  


def connect_wallet():
  it_exception = True
  while it_exception:
    try:
      wallet_icon = driver.find_element_by_class_name("css-16ehvw3")
      wallet_icon.click()

      it_exception = False
    except:
      it_exception = True
      time.sleep(0.1)
    
  it_exception = True
  while it_exception:
    try:
      mtmsk_connect = driver.find_elements_by_class_name("MuiListItemButton-root")
      mtmsk_connect[2].click()
      it_exception = False
    except:
      it_exception = True
      time.sleep(0.1)

  try:
    print("\n\n\n")
    time.sleep(1)
    print("time.sleep(1)")
    driver.switch_to.window(driver.window_handles[0])
    print("driver.switch_to.window(driver.window_handles[0])")
    modal = driver.find_element_by_class_name("popover-header__title")
    print("modal = driver.find_element_by_class_name(\"popover-header__title\")")
    driver.close()
    print("driver.close()")
    print("\n\n\n")
  except:
    pass

  time.sleep(3)
  driver.switch_to.window(driver.window_handles[1])



  it_exception = True
  while it_exception:
    try:
      mtmsk_next = driver.find_element_by_class_name("btn-primary")
      mtmsk_next.click()
      it_exception = False
    except:
      print("ERROR")
      it_exception = True
      time.sleep(0.1)
  it_exception = True
  while it_exception:
    try:
      mtmsk_connect = driver.find_element_by_class_name("btn-primary")
      mtmsk_connect.click()
      it_exception = False
    except:
      it_exception = True
      time.sleep(0.1)

  driver.switch_to.window(driver.window_handles[0])

  exception = True
  times = 0
  while exception:
    try:
      chng_polygon = driver.find_element_by_class_name("MuiListItemButton-root")
      chng_polygon.click()
      exception = False
      time.sleep(1)
    except:
      time.sleep(1)
      print("\n\n\n\n\nNo polygon found\n\n\n\n\n", str(times))
      times += 1
      if times > 3600:
        driver.close()
        raise Exception("Connecting wallet is taking too long")
  
  time.sleep(0.5)
  driver.switch_to.window(driver.window_handles[1])
  
  it_exception = True
  while it_exception:
    try:
      mtmsk_approve = driver.find_element_by_class_name("btn-primary")
      mtmsk_approve.click()
      it_exception = False
    except:
      it_exception = True
      time.sleep(0.1)

  it_exception = True
  while it_exception:
    try:
      mtmsk_connect = driver.find_element_by_class_name("btn-primary")
      mtmsk_connect.click()
      it_exception = False
    except:
      print("\n\n IS HERE \n\n")
      it_exception = True
      time.sleep(0.1)
  

  driver.switch_to.window(driver.window_handles[0])

def connect_wallet_2():
  wallet_icon = driver.find_element_by_class_name("css-16ehvw3")
  wallet_icon.click()
  time.sleep(2)
  mtmsk_connect = driver.find_elements_by_class_name("MuiListItemButton-root")
  mtmsk_connect[2].click()
  time.sleep(2)
  
  driver.switch_to.window(driver.window_handles[1])
  time.sleep(2)
  mtmsk_next = driver.find_element_by_class_name("btn-primary")
  mtmsk_next.click()
  time.sleep(2)
  mtmsk_connect = driver.find_element_by_class_name("btn-primary")
  mtmsk_connect.click()
  time.sleep(2)
  driver.switch_to.window(driver.window_handles[0])
  time.sleep(1)



def search_in_bar(search_bar, value):
  search_bar.clear()
  search_bar.send_keys(value)
  search_bar.send_keys(Keys.RETURN)

def fill_input(input_field, value):
  input_field.clear()
  input_field.send_keys(value)


def select_item_from_dropdown(dropdown, index):
  dropdown.select_by_index(index)

  
run_test()