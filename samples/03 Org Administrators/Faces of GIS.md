
#Faces of GIS

This sample notebook tries to re-create Esri's [Faces of GIS](https://www.flickr.com/photos/esri/sets/72157627065236829/) flickr stream, but using public ArcGIS Online profiles.

It iterates over a list of common last names and searches ArcGIS Online for users matching that name. If the user has a thumbnail, it display's the user's profile. 


    import pandas as pd
    from arcgis.gis import GIS
    from IPython.display import display


    df = pd.read_csv('data/lastnames.csv')
    df[:3]




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Surname</th>
      <th>Approximate</th>
      <th>%</th>
      <th>Rank</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>SMITH</td>
      <td>2,501,922</td>
      <td>1.006</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>JOHNSON</td>
      <td>2,014,470</td>
      <td>0.810</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>WILLIAMS</td>
      <td>1,738,413</td>
      <td>0.699</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




    gis = GIS()
    
    for index, row in df.iterrows():
        users = gis.users.search(row['Surname'])
        for u in users:
            if u['thumbnail'] is not None:
                display(u)


<div class="9item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/user.html?user=19allsmi' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/community/users/19allsmi/info/image.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right" style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/user.html?user=19allsmi' target='_blank'><b>Allison Smith</b>
                        </a>
                        <br><br><b>Bio</b>: 
                        <br><b>First Name</b>: Allison
                        <br><b>Last Name</b>: Smith
                        <br><b>Username</b>: 19allsmi
                        <br><b>Joined</b>: October 04, 2013
                        
                    </div>
                </div>
                



<div class="9item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/user.html?user=596117_onedu' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/community/users/596117_onedu/info/GetAttachment__284_29.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right" style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/user.html?user=596117_onedu' target='_blank'><b>Jasmin Smith</b>
                        </a>
                        <br><br><b>Bio</b>: 
                        <br><b>First Name</b>: Jasmin
                        <br><b>Last Name</b>: Smith
                        <br><b>Username</b>: 596117_onedu
                        <br><b>Joined</b>: September 23, 2014
                        
                    </div>
                </div>
                



<div class="9item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/user.html?user=918273645' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/community/users/918273645/info/58a7206a9eeb650d8f784521dfd783dc.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right" style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/user.html?user=918273645' target='_blank'><b>Smith Anwesson</b>
                        </a>
                        <br><br><b>Bio</b>: 
                        <br><b>First Name</b>: Smith
                        <br><b>Last Name</b>: Anwesson
                        <br><b>Username</b>: 918273645
                        <br><b>Joined</b>: November 14, 2012
                        
                    </div>
                </div>
                



<div class="9item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/user.html?user=600012083' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/community/users/600012083/info/arcgispic.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right" style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/user.html?user=600012083' target='_blank'><b>Richard Johnson</b>
                        </a>
                        <br><br><b>Bio</b>: Hello, my name is Ritchie Johnson.  I like Minecraft, LEGO, and Myst.  www.indianajones5390.weebly.com  www.twitter.com/indiajones5390  https://www.youtube.com/channel/UCUdCGDMg96YU69IPp_qGcYA  rcj5390@gmail.com  rcjsmurf@yahoo.com
                        <br><b>First Name</b>: Richard
                        <br><b>Last Name</b>: Johnson
                        <br><b>Username</b>: 600012083
                        <br><b>Joined</b>: April 07, 2016
                        
                    </div>
                </div>
                



<div class="9item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/user.html?user=a.johnson.GRHS' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/community/users/a.johnson.GRHS/info/x.jpeg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right" style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/user.html?user=a.johnson.GRHS' target='_blank'><b>Abby Johnson</b>
                        </a>
                        <br><br><b>Bio</b>: 
                        <br><b>First Name</b>: Abby
                        <br><b>Last Name</b>: Johnson
                        <br><b>Username</b>: a.johnson.GRHS
                        <br><b>Joined</b>: August 26, 2015
                        
                    </div>
                </div>
                



<div class="9item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/user.html?user=A.Johnson19' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/community/users/A.Johnson19/info/frost.png' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right" style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/user.html?user=A.Johnson19' target='_blank'><b>Anne Johnson</b>
                        </a>
                        <br><br><b>Bio</b>: GIS Coordinator University of Alaska Geographic Information Network
                        <br><b>First Name</b>: Anne
                        <br><b>Last Name</b>: Johnson
                        <br><b>Username</b>: A.Johnson19
                        <br><b>Joined</b>: October 28, 2010
                        
                    </div>
                </div>
                



<div class="9item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/user.html?user=621sterling' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/community/users/621sterling/info/Sterling.JPG' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right" style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/user.html?user=621sterling' target='_blank'><b>Sterling Burgess</b>
                        </a>
                        <br><br><b>Bio</b>: I have 15 year in information technology. My interest now is transitioning my information technology skills to the growing green industry, and I feel that I am a prime candidate. During the last year I have been studying, reading, watching videos, and compiling a list of sustainable Green industry companies websites, so I can stay abreast of the progress made within this industry.  I have also finished an online course on Energy in the Global Market Place, and a course in Disaster Preparedness. Also I am researching Everblue, which is a leading sustainability training institute worldwide. I am extremely passionate about being successful.  I have researched President Obamas green industry initiative, and Harry Reid, who replied to a letter from me explaining other avenues I should pursue. And I follow Van Jones, he is an American environmental advocate, and President of Rebuild the Dream.  My ultimate goal is to achieve the skill level of sustainable/green architect, and design buildings, homes, and retrofit all types of edifices. I believe my experience, and worldview will help me in any job.
                        <br><b>First Name</b>: Sterling
                        <br><b>Last Name</b>: Burgess
                        <br><b>Username</b>: 621sterling
                        <br><b>Joined</b>: May 01, 2014
                        
                    </div>
                </div>
                



<div class="9item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/user.html?user=a_jones' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/community/users/a_jones/info/IMG_0879.JPG' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right" style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/user.html?user=a_jones' target='_blank'><b>Alex Jones</b>
                        </a>
                        <br><br><b>Bio</b>: 
                        <br><b>First Name</b>: Alex
                        <br><b>Last Name</b>: Jones
                        <br><b>Username</b>: a_jones
                        <br><b>Joined</b>: December 14, 2011
                        
                    </div>
                </div>
                



<div class="9item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/user.html?user=12123232' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/community/users/12123232/info/purple_paw.png' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right" style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/user.html?user=12123232' target='_blank'><b>tt brown</b>
                        </a>
                        <br><br><b>Bio</b>: 
                        <br><b>First Name</b>: tt
                        <br><b>Last Name</b>: brown
                        <br><b>Username</b>: 12123232
                        <br><b>Joined</b>: January 25, 2016
                        
                    </div>
                </div>
                



<div class="9item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/user.html?user=154049' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/community/users/154049/info/bunny.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right" style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/user.html?user=154049' target='_blank'><b>Kylie Brown</b>
                        </a>
                        <br><br><b>Bio</b>: 
                        <br><b>First Name</b>: Kylie
                        <br><b>Last Name</b>: Brown
                        <br><b>Username</b>: 154049
                        <br><b>Joined</b>: August 21, 2015
                        
                    </div>
                </div>
                



<div class="9item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/user.html?user=5471gab' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/community/users/5471gab/info/ProfilePic.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right" style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/user.html?user=5471gab' target='_blank'><b>George Brown</b>
                        </a>
                        <br><br><b>Bio</b>: GIS Manager, GISP, Jacksonville Sheriff's Office Jacksonville, FL 25 Years working with ESRI Software.
                        <br><b>First Name</b>: George
                        <br><b>Last Name</b>: Brown
                        <br><b>Username</b>: 5471gab
                        <br><b>Joined</b>: November 09, 2010
                        
                    </div>
                </div>
                



<div class="9item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/user.html?user=aadavis1' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/community/users/aadavis1/info/GRHS_seal.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right" style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/user.html?user=aadavis1' target='_blank'><b>Adalia Davis</b>
                        </a>
                        <br><br><b>Bio</b>: 
                        <br><b>First Name</b>: Adalia
                        <br><b>Last Name</b>: Davis
                        <br><b>Username</b>: aadavis1
                        <br><b>Joined</b>: February 11, 2014
                        
                    </div>
                </div>
                



<div class="9item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/user.html?user=adaliadavis' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/community/users/adaliadavis/info/profile_150x150.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right" style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/user.html?user=adaliadavis' target='_blank'><b>Adalia Davis</b>
                        </a>
                        <br><br><b>Bio</b>: Areas of Interest: project based learning, multiple intelligence theory and geospatial technologies. For more information about me and what I do visit http://www.adaliadavis.com
                        <br><b>First Name</b>: Adalia
                        <br><b>Last Name</b>: Davis
                        <br><b>Username</b>: adaliadavis
                        <br><b>Joined</b>: May 25, 2011
                        
                    </div>
                </div>
                



<div class="9item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/user.html?user=adavisholland' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/community/users/adavisholland/info/alison.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right" style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/user.html?user=adavisholland' target='_blank'><b>Alison Davis-Holland</b>
                        </a>
                        <br><br><b>Bio</b>: 
                        <br><b>First Name</b>: Alison
                        <br><b>Last Name</b>: Davis-Holland
                        <br><b>Username</b>: adavisholland
                        <br><b>Joined</b>: March 23, 2011
                        
                    </div>
                </div>
                



<div class="9item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/user.html?user=@UnduhEstaMadeIt' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/community/users/@UnduhEstaMadeIt/info/C_3A_Documents_and_Settings_All_Users_Documents_My_Pictures_Sample_Pictures_495417219_L4uGk-S.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right" style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/user.html?user=@UnduhEstaMadeIt' target='_blank'><b>Trevor Miller</b>
                        </a>
                        <br><br><b>Bio</b>: 
                        <br><b>First Name</b>: Trevor
                        <br><b>Last Name</b>: Miller
                        <br><b>Username</b>: @UnduhEstaMadeIt
                        <br><b>Joined</b>: January 09, 2012
                        
                    </div>
                </div>
                



<div class="9item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/user.html?user=adriennemiller_NMHU' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/community/users/adriennemiller_NMHU/info/useless_map_4_el_jebel_flower_map.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right" style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/user.html?user=adriennemiller_NMHU' target='_blank'><b>Adrienne Miller</b>
                        </a>
                        <br><br><b>Bio</b>: 
                        <br><b>First Name</b>: Adrienne
                        <br><b>Last Name</b>: Miller
                        <br><b>Username</b>: adriennemiller_NMHU
                        <br><b>Joined</b>: August 11, 2015
                        
                    </div>
                </div>
                



<div class="9item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/user.html?user=194965' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/community/users/194965/info/download.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right" style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/user.html?user=194965' target='_blank'><b>Caitlin Wilson</b>
                        </a>
                        <br><br><b>Bio</b>: 
                        <br><b>First Name</b>: Caitlin
                        <br><b>Last Name</b>: Wilson
                        <br><b>Username</b>: 194965
                        <br><b>Joined</b>: August 21, 2015
                        
                    </div>
                </div>
                



<div class="9item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/user.html?user=218732' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/community/users/218732/info/images-1.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right" style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/user.html?user=218732' target='_blank'><b>M Wilson</b>
                        </a>
                        <br><br><b>Bio</b>: 
                        <br><b>First Name</b>: M
                        <br><b>Last Name</b>: Wilson
                        <br><b>Username</b>: 218732
                        <br><b>Joined</b>: November 11, 2014
                        
                    </div>
                </div>
                



<div class="9item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/user.html?user=8bitblood' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/community/users/8bitblood/info/Ralph.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right" style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/user.html?user=8bitblood' target='_blank'><b>Mike Moore</b>
                        </a>
                        <br><br><b>Bio</b>: All your bases are belong to us.
                        <br><b>First Name</b>: Mike
                        <br><b>Last Name</b>: Moore
                        <br><b>Username</b>: 8bitblood
                        <br><b>Joined</b>: January 24, 2013
                        
                    </div>
                </div>
                



<div class="9item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/user.html?user=amoore_idhs' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/community/users/amoore_idhs/info/pic.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right" style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/user.html?user=amoore_idhs' target='_blank'><b>Ashlee Moore</b>
                        </a>
                        <br><br><b>Bio</b>: 
                        <br><b>First Name</b>: Ashlee
                        <br><b>Last Name</b>: Moore
                        <br><b>Username</b>: amoore_idhs
                        <br><b>Joined</b>: September 21, 2011
                        
                    </div>
                </div>
                



<div class="9item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/user.html?user=41223taylor' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/community/users/41223taylor/info/C_3A_Users_Public_Pictures_Sample_Pictures_Koala.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right" style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/user.html?user=41223taylor' target='_blank'><b>Taylor Roseen</b>
                        </a>
                        <br><br><b>Bio</b>: 
                        <br><b>First Name</b>: Taylor
                        <br><b>Last Name</b>: Roseen
                        <br><b>Username</b>: 41223taylor
                        <br><b>Joined</b>: October 16, 2012
                        
                    </div>
                </div>
                



<div class="9item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/user.html?user=19ajand' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/community/users/19ajand/info/image.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right" style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/user.html?user=19ajand' target='_blank'><b>Aj Anderson</b>
                        </a>
                        <br><br><b>Bio</b>:  
                        <br><b>First Name</b>: Aj
                        <br><b>Last Name</b>: Anderson
                        <br><b>Username</b>: 19ajand
                        <br><b>Joined</b>: October 04, 2013
                        
                    </div>
                </div>
                



<div class="9item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/user.html?user=12CANSELL_Th' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/community/users/12CANSELL_Th/info/Gosden.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right" style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/user.html?user=12CANSELL_Th' target='_blank'><b>Thomas Cansell</b>
                        </a>
                        <br><br><b>Bio</b>: Sloth from goonies stunt man:   28 years young   Tesco suit for life 
                        <br><b>First Name</b>: Thomas
                        <br><b>Last Name</b>: Cansell
                        <br><b>Username</b>: 12CANSELL_Th
                        <br><b>Joined</b>: April 19, 2016
                        
                    </div>
                </div>
                



<div class="9item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/user.html?user=00032592' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/community/users/00032592/info/Screenshot_2015-09-24_at_3.33.50_PM.png' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right" style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/user.html?user=00032592' target='_blank'><b>Jackson Lufkin</b>
                        </a>
                        <br><br><b>Bio</b>: It's cha boi 
                        <br><b>First Name</b>: Jackson
                        <br><b>Last Name</b>: Lufkin
                        <br><b>Username</b>: 00032592
                        <br><b>Joined</b>: October 28, 2015
                        
                    </div>
                </div>
                



<div class="9item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/user.html?user=610059270' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/community/users/610059270/info/Depressing_Quotes__28Depression_Hurts_29_0082-0084__286_29.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right" style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/user.html?user=610059270' target='_blank'><b>kayla white</b>
                        </a>
                        <br><br><b>Bio</b>: 
                        <br><b>First Name</b>: kayla
                        <br><b>Last Name</b>: white
                        <br><b>Username</b>: 610059270
                        <br><b>Joined</b>: April 21, 2015
                        
                    </div>
                </div>
                



<div class="9item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/user.html?user=19leahar' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/community/users/19leahar/info/image.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right" style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/user.html?user=19leahar' target='_blank'><b>Leah Harris</b>
                        </a>
                        <br><br><b>Bio</b>: I love yellow lab puppyes they are so cute    and ador able    and I love unkle  sy  form duck dinsty      I have a dog    she is   lab and springer spanyal   and i had a cat  
                        <br><b>First Name</b>: Leah
                        <br><b>Last Name</b>: Harris
                        <br><b>Username</b>: 19leahar
                        <br><b>Joined</b>: October 04, 2013
                        
                    </div>
                </div>
                



<div class="9item_container" style="height: auto; overflow: hidden; border: 1px solid #cfcfcf; border-radius: 2px; background: #f6fafa; line-height: 1.21429em; padding: 10px;">
                    <div class="item_left" style="width: 210px; float: left;">
                       <a href='http://www.arcgis.com/home/user.html?user=2470akkmartinspr12' target='_blank'>
                        <img src='http://www.arcgis.com/sharing/rest/community/users/2470akkmartinspr12/info/profile.jpg' class="itemThumbnail">
                       </a>
                    </div>
        
                    <div class="item_right" style="float: none; width: auto; overflow: hidden;">
                        <a href='http://www.arcgis.com/home/user.html?user=2470akkmartinspr12' target='_blank'><b>Anna Martin</b>
                        </a>
                        <br><br><b>Bio</b>: 
                        <br><b>First Name</b>: Anna
                        <br><b>Last Name</b>: Martin
                        <br><b>Username</b>: 2470akkmartinspr12
                        <br><b>Joined</b>: January 16, 2012
                        
                    </div>
                </div>
                



    ---------------------------------------------------------------------------
    

    KeyboardInterrupt: 


An org administrator can search for users in a similar manner, and even update their properties.


    
