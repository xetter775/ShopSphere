from django.urls import path,include
from .views import (
    ItemDetailView,
    HomeView,
    add_to_cart,
    remove_from_cart,
    ShopView,
    OrderSummaryView,
    remove_single_item_from_cart,
    CheckoutView,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    CategoryView,
    ProfileDashboardView,
    UserOrdersView,
    OrderDetailView,
    RequestRefundView,
    CancelOrderView,
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('category/<slug>/', CategoryView.as_view(), name='category'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add_coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    # this is for user pannel
    path('profile/', ProfileDashboardView.as_view(), name='profile_dashboard'),
    path('profile/orders/', UserOrdersView.as_view(), name='user_orders'),
    path('profile/orders/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('profile/refund/<int:pk>/', RequestRefundView.as_view(), name='request_refund'),
    path('profile/cancel/<int:pk>/', CancelOrderView.as_view(), name='cancel_order'),

]
