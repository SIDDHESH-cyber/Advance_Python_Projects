import matplotlib.pyplot as plt

def line_graph_1():  
    x = [1,6]
    y = [6,1]

    a=[1,6]  
    b=[1,3]

    i=[3,3]  
    j=[6,1]  
    plt.plot(x,y,label="line_1",marker = 'o')
    plt.plot(a,b,label="line_2")  
    plt.plot(i,j,label="line_3")  

    plt.title('My First Graph')

    plt.xlabel('X - Axis')
    plt.ylabel('Y - Axis')
    
    plt.show()

def line_graph_2():  
    x = [1,6,1,5]
    y = [6,1,1,3]

    a=[1,3,6]  
    b=[1,4,6]

    i=[3,3]  
    j=[6,1]  
    plt.plot(x,y,label="line_1")
    plt.plot(a,b,label="line_2",linestyle='dotted',color='black')  
    plt.plot(i,j,label="line_3",linestyle='dashed')  

    font_color = {'family':'serif','color':'red','size':25}

    plt.title('My Second Graph',fontdict=font_color)

    plt.xlabel('X - Axis')
    plt.ylabel('Y - Axis')
    
    plt.grid()

    plt.show()

def line_graph_3():
    #?_________Plot_1________
    x = [0, 1, 2, 3]
    y = [3, 8, 1, 10]

    plt.subplot(2, 1, 1)
    plt.plot(x,y)

    plt.title('My Third Graph')

    #?_________Plot_2________
    x = [0, 1, 2, 3]
    y = [10, 20, 30, 40]

    plt.subplot(2, 1, 2)

    
    plt.xlabel('X - Axis')
    plt.ylabel('Y - Axis')
    
    plt.plot(x,y)

    plt.show()

def scatter_graph():
    
    x = [0, 1, 2, 3]
    y = [10, 20, 30, 40]    
    plt.scatter(x, y,color='purple',s=300)

    x = [1,6,1,5]
    y = [6,1,1,3]
    plt.scatter(x, y,color='red')
    
    plt.title('My Fourth Graph')
    
    plt.xlabel('X - Axis')
    plt.ylabel('Y - Axis')
    
    plt.show()

def bar_graph():
    x=["A","B","C","D"]
    y=[10,50,5,35]
    
    plt.bar(x,y)
    # plt.bar(x,y,width=0.1)
    # plt.barh(x,y) #x and y axis are replaced 
    # plt.barh(x,y,height=0.1) #barh takes height 
    
    plt.title('My Fifth Graph')
    
    plt.xlabel('Names')
    plt.ylabel('Percentages')

    plt.show()

def pie_chart():
    pie=[15,25,35,25]
    lab=["Food","Gym","Games","Cycling"]
    brk=[0,0,0,0.2]
    
    plt.pie(pie,labels=lab,startangle=180,explode=brk,shadow=True,colors=['r','m','c','b'])

    plt.legend()

    plt.title('My Sixth Graph')

    plt.show()


if __name__ == "__main__":
    line_graph_1()  
    line_graph_2()  
    line_graph_3()  
    scatter_graph()
    bar_graph()  
    pie_chart()
