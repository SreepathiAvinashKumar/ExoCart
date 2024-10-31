![image](https://github.com/SreepathiAvinashKumar/ExoCart/blob/master/Website%20images/Screenshot1.png?raw=true)
ExoCart is a comprehensive e-commerce website designed to facilitate seamless user and seller interactions. Built using Django as the backend framework and styled with **Django-Tailwind**, the platform provides a modern, responsive, and highly scalable solution for online shopping experiences. This project includes a variety of essential e-commerce features, aimed at improving both the user experience and system efficiency for buyers and sellers.

One of the core functionalities allows sellers to easily add items to the platform, with detailed product descriptions, pricing, and image uploads made possible through the **Pillow** Python library. Buyers can browse products and utilize key features like **Add to Cart** and **Wishlist**, offering flexibility for saving their favorite products for future purchases.

A key feature of the platform is the **Checkout** process, implemented using payment gateway integration with Razorpay. By setting up a dummy Razorpay account, users can securely process payments, with real-time updates on transaction status. This ensures a smooth, secure, and efficient checkout experience for buyers. The **razorpay** Python package was crucial in integrating this functionality.

User authentication is another integral part of the system, providing secure Login and Logout functionalities using Django’s built-in authentication system. To enhance the design and user experience, I incorporated **django-crispy-forms** along with **crispy-bootstrap4**, ensuring the website’s forms are responsive and visually appealing.

I utilized **Django-Tailwind** to build the frontend, ensuring a clean and modern UI that adapts seamlessly across devices. Tailwind CSS helped me focus on rapid frontend development while maintaining consistency and customization options throughout the application.

Here’s a list of the key Python modules I used for this project:

```
pip install django
pip install Pillow
pip install django-crispy-forms
pip install crispy-bootstrap4
pip install razorpay
pip install django-tailwind
```

Overall, this project serves as a complete, fully functional e-commerce platform, providing a well-designed and user-friendly experience. With its integration of authentication, secure payments, and modern frontend styling using Django-Tailwind, the platform is scalable, secure, and maintainable for future enhancements.

Working on 

1. Arrange the Products via Categories in the home page
2. Add the products to the ecommerce 
3. Change the Order page Logo 
4. Change the favicon icon of the ecommerce.
5. change the title of the page
6. Discount and Tax Adding to the cart page
