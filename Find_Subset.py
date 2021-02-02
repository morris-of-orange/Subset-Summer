# -*- coding: utf-8 -*-


def Find_Sub_Pool(Pool,Subtotal,top_level=True):
    output=[]
    use_compliment=False
    sub_finder = Subtotal
    #For stuff we only want to do in the first iteration
    if top_level:
        #We want the list to go from high to low
        Pool.sort()
        Pool.reverse()
        
        #TODO: fix this for the user
        #for now, it only takes integer, this removes the roundoff error. 
        #I'm half drunk when I Code, I'm not smart enough to do this. 
        reject=False
        if not(isinstance(Subtotal,int)):
            raise ValueError('Your Subtotal needs to be an integer, it is not an integer')
        for i in Pool:
            reject = reject or not(isinstance(i,int)) 
        if reject:
            raise ValueError('Your list has an non integer, this only works with integer due to roundoff errors.')

        
    
    #if our list is [1,2,3] and our Subtotal is 2, we know it's not 3, so remove it
    Pool = [i for i in Pool if i <= Subtotal]    
    Pool_Sum=sum(Pool)
    
    Compliment= Pool_Sum-Subtotal
    
        
    
    if len(Pool)==0:
        output = []
    #If we removed all the elements, then we have a bad day. 
    #This is when the entire pool is good. E.g. search for 6 in [1,2,3]
    elif Pool_Sum==Subtotal:
        output= Pool.copy()
    #If we know that the subtotal cannot be in the Pool E.g. 6 in [1,2,2] because the pool
    #Sums to 5 we know that the subtotal is not in the pool. 
    elif Pool_Sum < Subtotal:
        output= []
    elif Subtotal in Pool:
        output= [Subtotal]
    elif Compliment in Pool:
        output=Pool.copy()
        output.remove(Compliment)
    

    else:
        #so our number isn't in the pool but it could be the sum of some numbers in our pool 
        
        #it is easier to find the compliment if it is less than the subtotal. 
        # e.g. it is easer to find 2 than 15 in [1,1,4,5,6] becausse by removing 
        #any numbers above 2 we get [1,1] which sums to 2 so we hit the first if statement above
        #as opposed to going down the tree to we get [4,5,6]
        #This matters if the answer is like a sum of 90% of the Pool
        if Compliment < Subtotal:
            sub_finder = Compliment
            use_compliment=True #keep track of if we are looking for the compliment, or the actual
            
        for i in Pool:
            #for each element, we search again but for the remainder
            #e.g. if we are searching for 5 in[1,1,2,3], now we will search for 2=5-3 in [1,1,2]
            #if the subpool dosen't have it, we will move on, but if it does, then we will go back up
            hottub= Pool.copy()
            hottub.remove(i)   
            Subpool = Find_Sub_Pool(hottub,sub_finder-i,False)
            if len(Subpool)>0:
                Subpool.append(i)
                output = Subpool
                break
   
    #So the Compliment was less than the Subtotal,
    if use_compliment:
        if len(output)==0:
            return [] #if we couldn't find any
        else:
            reverse = [i for i in Pool if i not in output]
            output = reverse.copy()

    if top_level:
        #We want the list to go from high to low
        output.sort()
        output.reverse()

    return output
