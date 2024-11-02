from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        # from allauth.account.utils import user_email, user_field, user_username

        data = form.cleaned_data

        # 기본 저장 필드: first_name, last_name, username, email
        user = super().save_user(request, user, form, False)
        
        # 추가 저장 필드
        # nickname 필드를 추가
        mainbank = data.get('mainbank', '')
        register = data.get('register', '')
        work = data.get('work', '')
        salary = data.get('salary', '')
        money = data.get('money', '')
        financial_products = data.get('financial_products', '')

        
        if mainbank:
            user.mainbank = mainbank
        if register:
            user.register = register
        if work:
            user.work = work
        if salary:
            user.salary = salary
        if money:
            user.money = money
        if financial_products:
            user.financial_products = financial_products

        print('========================================')
        print(user)
        print('========================================')
        user.save()
        return user