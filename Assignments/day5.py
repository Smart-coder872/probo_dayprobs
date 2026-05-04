P_x = [0.985, 0.015] #not faulty, faulty
P_x_z = [1/3, 1] #not faulty, faulty
k = 10 #number of steps

def bayes_filter(x_z, x):
    #bayes filter without normalization
    P_not_faulty_num = x_z[0]*x[0] #faulty
    P_faulty_num = x_z[1]*x[1]     #not faulty

    #Normalization
    norm = P_not_faulty_num + P_faulty_num

    #bayes filter with normalization
    P_not_faulty = P_not_faulty_num/norm
    P_faulty = P_faulty_num/norm
    
    return P_not_faulty, P_faulty

values = []

prior = bayes_filter(P_x_z, P_x) 
values.append(f"Filtered Estimate for k=1: [{prior[0]} {prior[1]}]")

for i in range(2,k+1):
    new_prior = bayes_filter(P_x_z, prior)
    values.append(f"Filtered Estimate for k={i}: [{new_prior[0]} {new_prior[1]}]")
    prior = new_prior

print('\n'.join(values)) #make new line for each value


    