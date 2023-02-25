from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=50, blank=True)


class Food(models.Model):
    name = models.CharField(max_length=20) 
    price=models.DecimalField(max_digits=3,decimal_places=0) # decimal_places小數點位數
    comment = models.CharField(max_length=50, blank=True) # blank允許欄位為空
    is_spicy = models.BooleanField(default=False) 
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

# 詳細資料庫CRUD操作參考 https://ithelp.ithome.com.tw/articles/10212427

class Comment(models.Model):
    content = models.CharField(max_length=200)
    visitor = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    date_time = models.DateTimeField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    class Meta: # 新增權限 每一個權限都會跟一個資料庫模型綁定
            ordering = ['date_time']
            permissions = (
                ("can_comment", "Can comment"),  # 只有一個權限時，千萬不要忘了逗號！
                # 第一個元素是codename字串(實際運用在代碼中的權限名稱)，第二個元素是name字串(用戶名稱，通常只是拿來顯示，好閱讀的)
            )