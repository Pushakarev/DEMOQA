import random
import time
from locators.interaction_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DropPageLocators, DraggablePageLocators
from pages.base_page import BasePage

class SortablePage(BasePage):
    locators= SortablePageLocators()

    def get_sortable(self,elements):
        item_ist = self.elements_are_visable(elements)
        return [item.text for item in item_ist]

    def change_list(self):
        self.element_is_visable(self.locators.TAB_LIST).click()
        order_before = self.get_sortable(self.locators.LIST_ITEM)
        item_list = random.sample(self.elements_are_visable(self.locators.LIST_ITEM),k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_drop_to_element(item_what,item_where)
        order_after = self.get_sortable(self.locators.LIST_ITEM)
        return order_before, order_after

    def change_list_in_grid(self):
        self.element_is_visable(self.locators.TAB_GRID).click()
        order_before = self.get_sortable(self.locators.LIST_TAB_GRID)
        item_list = random.sample(self.elements_are_visable(self.locators.LIST_TAB_GRID), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_drop_to_element(item_what, item_where)
        order_after = self.get_sortable(self.locators.LIST_TAB_GRID)
        return order_before, order_after

class SelectablePage(BasePage):
    locators= SelectablePageLocators()

    def click_selectable(self,elements):
        item_list = self.elements_are_visable(elements)
        random.sample(item_list, k=1)[0].click()

    def selected_list_item(self):
        self.element_is_visable(self.locators.TAB_LIST).click()
        self.click_selectable(self.locators.LIST_ITEM)
        active_elements= self.element_is_visable(self.locators.LIST_ITEM_ACTIVE)
        return active_elements.text

    def selected_grid_item(self):
        self.element_is_visable(self.locators.TAB_GRID).click()
        self.click_selectable(self.locators.LIST_TAB_GRID)
        active_elements = self.element_is_visable(self.locators.LIST_TAB_GRID_ACTIVE)
        return active_elements.text

class ResizablePage(BasePage):
    locators= ResizablePageLocators()

    def size_of_window(self,value_of_window):
        width =value_of_window
        height =value_of_window
        return width, height

    def get_max_min_size(self,element):
        size = self.element_is_visable(element)
        size_value= size.get_attribute('style')
        return size_value

    def change_size_big_box(self):
        self.action_drag_drop(self.element_is_visable(self.locators.BIG_BOX_HANDLE),400,200)
        big_max_size= self.size_of_window(self.get_max_min_size(self.locators.BIG_BOX))
        self.action_drag_drop(self.element_is_visable(self.locators.BIG_BOX_HANDLE), -400, -200)
        big_min_size = self.size_of_window(self.get_max_min_size(self.locators.BIG_BOX))
        return big_max_size, big_min_size

    def change_size_small_box(self):
        self.action_drag_drop(self.element_is_visable(self.locators.SAMLL_BOX_HANDLE), 400, 200)
        max_size = self.size_of_window(self.get_max_min_size(self.locators.SMALL_BOX))
        self.action_drag_drop(self.element_is_visable(self.locators.SAMLL_BOX_HANDLE), -400, -200)
        min_size = self.size_of_window(self.get_max_min_size(self.locators.SMALL_BOX))
        return max_size, min_size

class DropPage(BasePage):
    locators= DropPageLocators()

    def drop_simple (self):
        drag_div = self.element_is_visable(self.locators.DRAG_ME_SIMPLE)
        drop_div = self.element_is_visable(self.locators.DROP_ME_SIMPLE)
        self.action_drag_drop_to_element(drag_div,drop_div)
        return drop_div.text

    def drop_accept (self):
        self.element_is_visable(self.locators.ACCEPT_TAB).click()
        drag_div = self.element_is_visable(self.locators.DRAG_ME_ACCEPT)
        drop_div = self.element_is_visable(self.locators.DROP_ME_ACCEPT)
        self.action_drag_drop_to_element(drag_div, drop_div)
        time.sleep(2)

        return drop_div.text

    def drop_not_accept(self):
        self.element_is_visable(self.locators.ACCEPT_TAB).click()
        drag_div = self.element_is_visable(self.locators.DRAG_ME_NOTACCEPT)
        drop_div = self.element_is_visable(self.locators.DROP_ME_ACCEPT)
        self.action_drag_drop_to_element(drag_div, drop_div)
        time.sleep(2)
        return drop_div.text

    def drop_prevent_propogation(self):
        self.element_is_visable(self.locators.PREVENT_TAB).click()
        drag_div = self.element_is_visable(self.locators.DRAG_ME_PREVENT)
        drop_greedy_div = self.element_is_visable(self.locators.DROP_ME_GREEDY)
        drop_not_greedy_div = self.element_is_visable(self.locators.DROP_ME_NOT_GREEDY)
        self.action_drag_drop_to_element(drag_div, drop_not_greedy_div)
        text_not_greedy_after = self.element_is_visable(self.locators.DROP_ME_NOT_GREEDY_TEXT).text
        self.action_drag_drop_to_element(drag_div, drop_greedy_div)
        text_greedy_after = self.element_is_visable(self.locators.DROP_ME_GREEDY_TEXT).text
        text_greedy_before = drop_greedy_div.text
        text_not_greedy_before= drop_not_greedy_div.text
        return text_greedy_before, text_not_greedy_before,text_greedy_after,text_not_greedy_after

    def drop_revert(self):
        self.element_is_visable(self.locators.REVENT_TAB).click()
        drop_div = self.element_is_visable(self.locators.DROP)
        drag_revent_div = self.element_is_visable(self.locators.DRAG_WILL_REVENT)
        self.action_drag_drop_to_element(drag_revent_div, drop_div)
        position_before = drag_revent_div.get_attribute('style')
        time.sleep(1)
        position_after = drag_revent_div.get_attribute('style')
        return position_before, position_after

    def drop_not_revert(self):
        self.element_is_visable(self.locators.REVENT_TAB).click()
        drop_div = self.element_is_visable(self.locators.DROP)
        drag_not_revent_div = self.element_is_visable(self.locators.DRAG_WILL_NOT_REVENT)
        self.action_drag_drop_to_element(drag_not_revent_div,drop_div )
        position_before = drag_not_revent_div.get_attribute('style')
        time.sleep(1)
        position_after = drag_not_revent_div.get_attribute('style')
        return position_before, position_after
class DraggablePage(BasePage):
    locators =DraggablePageLocators()


    def draggable1_check(self):

        drag_element = self.element_is_visable(self.locators.SIMPLE_DRAG)
        self.action_drag_drop(drag_element, 50, 20)
        position_before= drag_element.get_attribute ('style')
        self.action_drag_drop(drag_element, 50, 20)
        position_after = drag_element.get_attribute('style')
        return position_before, position_after

    def draggable_check_axis(self):
        self.element_is_visable(self.locators.AXIS_TAB).click()
        drag_elementx = self.element_is_visable(self.locators.ONLY_X)
        self.action_drag_drop(drag_elementx, 50, 0)
        position_beforex= drag_elementx.get_attribute ('style')
        self.action_drag_drop(drag_elementx, 50, 0)
        position_afterx = drag_elementx.get_attribute('style')
        drag_elementy = self.element_is_visable(self.locators.ONLY_Y)
        self.action_drag_drop(drag_elementy, 0, 20)
        position_beforey = drag_elementy.get_attribute('style')
        self.action_drag_drop(drag_elementy, 0, 20)
        position_aftery = drag_elementy.get_attribute('style')
        return position_beforex, position_afterx,position_beforey, position_aftery












































