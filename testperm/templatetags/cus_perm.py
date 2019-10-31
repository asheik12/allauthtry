from django.template import Library

register = Library()

@register.filter('get_content')
def get_content(user, value):
    list_perm = ['testperm.view_employee', 'testperm.add_employee', 'testperm.change_employee', 'testperm.delete_employee']
    val = 'testperm.'+ value +'_employee'
    if val in list_perm:
        if user.has_perm(val):
            return True
        else:
            return False    
    else:
        return False        
       
    # return user.get_all_permissions()