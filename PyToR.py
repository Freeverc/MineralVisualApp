import rpy2.robjects as robjects


def goto_r():
    r_script = '''
                library(aplpack) 
                library(openxlsx)
                cur_data<-read.xlsx("cur_data.xlsx", sheet = 1)
                print("read sucess")
                # 保存图片
                png('face.png')
                col_num=ncol(cur_data)
                face_model=faces(cur_data[,3:col_num],labels=cur_data[[2]])
                dev.off()
                # 导出数据
                cur_data=data.frame(face_model$info)
                write.csv(cur_data,'face_info.csv',row.names=F,col.names=F,sep='')
               '''
    robjects.r(r_script)

goto_r()