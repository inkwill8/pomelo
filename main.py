import urls as u
import components as cp

amzn_url = u.urls[0]["amzn_url"]
newegg_url = u.urls[0]["newegg_url"]
bb_url = u.urls[0]["bb_url"]

cpu = cp.Component('Ryzen 9 9950X3D', amzn_url, newegg_url, bb_url, cp.ComponentType.cpu)
newegg_price = cpu.get_newegg_price(cpu.newegg_url, u.headers)
bb_price = cpu.get_bb_price(cpu.bb_url, u.headers)
cpu.set_newegg_price(newegg_price)
print(cpu.name + ' ' + cpu.type.value + ' ')
print(f'Newegg Price:  {cpu.newegg_price}')
print(f'Best Buy Price:  {cpu.bb_price}')


