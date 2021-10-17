import numpy as np
import matplotlib.pyplot as plt


# https://www.engineeringtoolbox.com/hazen-williams-coefficients-d_798.html


hazen_williams_coef_dict = { 

'Acrylonite Butadiene Styrene' : 130,
'Aluminum' : 130,
'Asbestos Cement' : 140,
'Asphalt Lining' : 130,
'Brass' : 130,
'Brick sewer' : 90,
'Cast-Iron - new unlined (CIP)' : 130,
'Cast-Iron 10 years old' : 107,
'Cast-Iron 20 years old' : 89,
'Cast-Iron 30 years old' : 75,
'Cast-Iron 40 years old' : 64,
'Cast-Iron, asphalt coated' : 100,
'Cast-Iron, cement lined' : 140,
'Cast-Iron, bituminous lined' : 140,
'Cast-Iron, sea-coated' : 120,
'Cast-Iron, wrought plain' : 100,
'Cement lining' : 130,
'Concrete' : 100,
'Concrete lined, steel forms' : 140,
'Concrete lined, wooden forms' : 120,
'Concrete, old' : 100,
'Copper' : 130,
'Corrugated Metal' : 60,
'Ductile Iron Pipe (DIP)' : 140,
'Ductile Iron, cement lined' : 120,
'Fiber' : 140,
'Fiber Glass Pipe - FRP' :150,
'Galvanized iron' :120,
'Glass' :130,
'Lead': 130,
'Metal Pipes - Very to extremely smooth' : 130,
'Plastic' : 130,
'Polyethylene, PE, PEH' : 140,
'Polyvinyl chloride, PVC, CPVC': 150,
'Smooth Pipes' : 140,
'Steel new unlined' : 140,
'Steel, corrugated' : 60,
'Steel, welded and seamless' : 100,
'Steel, interior riveted, no projecting rivets' : 110,
'Steel, projecting girth and horizontal rivets' : 100,
'Steel, vitrified, spiral-riveted' : 90,
'Steel, welded and seamless' : 100,
'Tin' : 130,
'Vitrified Clay' : 110,
'Wrought iron, plain' : 100,
'Wooden or Masonry Pipe - Smooth' : 120,
'Wood Stave ': 110
}

#used schedule 40 steel pipe inner diameters for example
# https://www.archtoolbox.com/materials-systems/plumbing/standard-pipe-dimensions.html

inner_diameter_dict = {

'1/8' : 0.269,
'1/4' : 0.364,
'3/8' : 0.493,
'1/2' : 0.622,
'3/4' : 0.824,
'1' : 1.049,
'1-1/4' : 1.660,
'1-1/2' : 1.900,
'2' : 2.375,
'2-1/2' : 2.875,
'3' : 3.500,
'3-1/2' : 4.000,
'4' : 4.500,
'5' : 5.563,
'6' : 6.625,
'8' : 8.625,
'10' : 10.750,
'12' : 12.75,
'14' : 14.000,
'16' : 16.000,
'18' : 18.000,
'20' : 20.000,
'24' :24.0
}



def plot_head(inner_diameter, pipe_length, material):
    
    
    
    flow_rates = np.arange(1,1000)
    
    #hazen-williams equation
    #pipe_length (feet)
    #flow_rate (gal/min)
    #inner diamter (inches)
    head_loss = [4.73*((flow_rate/hazen_williams_coef_dict[material])**1.852)*(pipe_length/(inner_diameter_dict[inner_diameter]**4.87)) for flow_rate in flow_rates]
    
    #figure
    plt.figure(figsize = (10,8))
    plt.plot(flow_rates, head_loss, label = material)
    plt.title(f'Head Loss for {inner_diameter} inch {material} pipe', fontsize = (20))
    plt.xlabel('Flow Rate (gal/min)')
    plt.ylabel('Head Loss')
    plt.legend()
    plt.show()
    
    return head_loss

plot_head('2', 100, 'Steel new unlined')


