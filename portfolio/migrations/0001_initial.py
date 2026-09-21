from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(name="Profile", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("name", models.CharField(default="Your Name", max_length=100)), ("title", models.CharField(default="Graphic Designer", max_length=120)),
            ("availability", models.CharField(default="Available for freelance", max_length=120)), ("hero_heading", models.CharField(default="Graphic design that speaks louder than words.", max_length=180)),
            ("hero_text", models.TextField(default="Branding, posters, social media, and visual identity — crafted with bold ideas and pixel-perfect detail.")),
            ("about_text", models.TextField(default="Hi, I'm Your Name — a graphic designer with a passion for bold, clean, and meaningful visuals. I help brands tell their story through design that stands out.")),
            ("about_detail", models.TextField(default="With years of experience across branding, digital, and print, I turn ideas into visuals that connect.")),
            ("about_image_url", models.URLField(default="https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=800&q=80")), ("skills", models.CharField(default="Adobe Photoshop, Illustrator, Figma, InDesign, After Effects, Branding", max_length=500)),
            ("email", models.EmailField(default="hello@yourname.com", max_length=254)), ("phone", models.CharField(default="+1 234 567 890", max_length=50)), ("whatsapp", models.CharField(default="+1 987 654 321", max_length=50)), ("office", models.CharField(blank=True, default="+1 122 334 455", max_length=50)),
            ("instagram_url", models.URLField(blank=True)), ("behance_url", models.URLField(blank=True)), ("dribbble_url", models.URLField(blank=True))], options={"verbose_name": "Portfolio profile"}),
        migrations.CreateModel(name="Project", fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("title", models.CharField(max_length=150)), ("description", models.TextField()), ("category", models.CharField(max_length=80)), ("image_url", models.URLField(help_text="Direct URL to the project image")), ("featured", models.BooleanField(default=True)), ("order", models.PositiveIntegerField(default=0))], options={"ordering": ["order", "-id"]}),
    ]
