###
CMS
###

Dynamically create a menu
=========================

* Create menu.py with following content

from menus.base import NavigationNode
from cms.menu_bases import CMSAttachMenu
from menus.menu_pool import menu_pool
from django.core.urlresolvers import reverse
from myapp.models import Category

class CategorieMenu(CMSAttachMenu):
    name = "Categories Menu"

    def get_nodes(self, request):
        nodes = []

        for category in Category.objects.all():
            nodes.append(NavigationNode(category.name,
                                        reverse("category_list", kwargs={"category": category.name}),
                                        category.pk,
                                    ))

        return nodes

menu_pool.register_menu(CategorieMenu)
