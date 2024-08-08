from selenium.webdriver.common.by import By

class SortablePageLocators:
    TAB_LIST= (By.CSS_SELECTOR,"a[id='demo-tab-list']")
    LIST_ITEM= (By.CSS_SELECTOR,"div[id='demo-tabpane-list']  div[class='list-group-item list-group-item-action']")
    TAB_GRID= (By.CSS_SELECTOR,"a[id='demo-tab-grid']")
    LIST_TAB_GRID = (By.CSS_SELECTOR,"div[id='demo-tabpane-grid'] div[class='list-group-item list-group-item-action']")

class SelectablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, "a[id='demo-tab-list']")
    LIST_ITEM = (By.CSS_SELECTOR, "li[class='mt-2 list-group-item list-group-item-action']")
    LIST_ITEM_ACTIVE= (By.CSS_SELECTOR, "li[class='mt-2 list-group-item active list-group-item-action']")
    TAB_GRID = (By.CSS_SELECTOR, "a[id='demo-tab-grid']")
    LIST_TAB_GRID = (By.CSS_SELECTOR, "li[class='list-group-item list-group-item-action']")
    LIST_TAB_GRID_ACTIVE= (By.CSS_SELECTOR, "li[class='list-group-item list-group-item-action']")

class ResizablePageLocators:
    BIG_BOX = (By.CSS_SELECTOR, "div[id='resizableBoxWithRestriction']")
    SMALL_BOX = (By.CSS_SELECTOR, "div[id='resizable']")
    BIG_BOX_HANDLE = (By.CSS_SELECTOR, "div[id ='resizableBoxWithRestriction'] span[class='react-resizable-handle react-resizable-handle-se']")
    SAMLL_BOX_HANDLE = (By.CSS_SELECTOR, "div[id ='resizable'] span[class='react-resizable-handle react-resizable-handle-se']")

class DropPageLocators:
    # simple
    SIMPLE_TAB  = (By.CSS_SELECTOR, "a[id='droppableExample-tab-simple']")
    DRAG_ME_SIMPLE  = (By.CSS_SELECTOR, "div[id='draggable']")
    DROP_ME_SIMPLE  = (By.CSS_SELECTOR, "div[class='simple-drop-container'] div[id='droppable']")
    # accept
    ACCEPT_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-accept']")
    DRAG_ME_ACCEPT = (By.CSS_SELECTOR, "div[id='acceptable']")
    DRAG_ME_NOTACCEPT = (By.CSS_SELECTOR, "div[id='notAcceptable']")
    DROP_ME_ACCEPT = (By.CSS_SELECTOR, "div[class='accept-drop-container'] div[id='droppable']")
    # prevent
    PREVENT_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-preventPropogation']")
    DRAG_ME_PREVENT = (By.CSS_SELECTOR, "div[id='dragBox']")
    DROP_ME_NOT_GREEDY = (By.CSS_SELECTOR, "div[id='notGreedyInnerDropBox']")
    DROP_ME_NOT_GREEDY_TEXT = (By.CSS_SELECTOR, "div[id='notGreedyDropBox'] p:nth-child(1)")
    DROP_ME_GREEDY = (By.CSS_SELECTOR, "div[id='greedyDropBoxInner']")
    DROP_ME_GREEDY_TEXT = (By.CSS_SELECTOR, "div[id='greedyDropBoxInner'] p:nth-child(1)")
    # revent draggable
    REVENT_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-revertable']")
    DRAG_WILL_REVENT = (By.CSS_SELECTOR, "div[id='revertable']")
    DRAG_WILL_NOT_REVENT = (By.CSS_SELECTOR, "div[id='notRevertable']")
    DROP =  (By.CSS_SELECTOR, " div[id='revertableDropContainer'] div[id='droppable']")

class DraggablePageLocators:
    SIMPLE_DRAG = (By.CSS_SELECTOR, "div[id='dragBox']")
    AXIS_TAB = (By.CSS_SELECTOR, "a[id='draggableExample-tab-axisRestriction']")
    ONLY_X = (By.CSS_SELECTOR, "div[id='restrictedX']")
    ONLY_Y = (By.CSS_SELECTOR, "div[id='restrictedY']")
















