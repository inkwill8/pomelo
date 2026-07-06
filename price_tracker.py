import urls as u
import components as cp

cpu = cp.Component('Ryzen 9 9950X3D', u.urls[0]["newegg_url"], cp.ComponentType.cpu)
newegg_price = cpu.get_newegg_price(cpu.url, u.headers)
cpu.set_newegg_price(newegg_price)
print(cpu.name + ' ' + cpu.type + ' ' + cpu.newegg_price)


