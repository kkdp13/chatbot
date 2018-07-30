def caratsize(carat):

    port=float(carat)
    if port < 10:
        if port < 5:
            if port < 4:
                if port < 3:
                    if port < 2:
                        if port < 1.5:
                            if port < 1:
                                if port < 0.9:
                                    if port < 0.7:
                                        if port < 0.5:
                                            if port < 0.4:
                                                if port < 0.3:
                                                    if port < 0.23:
                                                        if port < 0.18:
                                                            if port < 0.15:
                                                                if port < 0.08:
                                                                    if port < 0.04:
                                                                        #print("port 0.01")
                                                                        return 0.01
                                                                    else:
                                                                        #print("port 0.04")
                                                                        return 0.04
                                                                else:
                                                                    #print("port 0.08")
                                                                    return 0.08
                                                            else:
                                                                #print("port 0.15")
                                                                return 0.15
                                                        else:
                                                            #print("port 0.18")
                                                            return 0.18
                                                    else:
                                                        #print("port 0.23")
                                                        return 0.23
                                                else:
                                                    #print("port 0.3")
                                                    return 0.3
                                            else:
                                                #print("port 0.4")
                                                return 0.4
                                        else:
                                            #print("port 0.5")
                                            return 0.5
                                    else:
                                        #print("port 0.7")
                                        return 0.7
                                else:
                                    #print("port 0.9")
                                    return 0.9
                            else:
                                #print("port 1")
                                return 1
                        else:
                            #print("port 1.5")
                            return 1.5
                    else:
                        #print("port 2")
                        return 2
                else:
                    #print("port 3")
                    return 3
            else:
                #print("port 4")
                return 4
        else:
            #print("port 5")
            return 5
    else:
        #print("port 10")
        return 10