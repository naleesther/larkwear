import React,{ useEffect,useState} from  "react";
//https://dummyjson.com/docs/users


const User = () =>{
    const [user,setUser] =useState();
    const [loading,setLoading]=useState(false);

    useEffect(()=>{
        userData();

    },[]);
    const userData=()=>{
    fetch("https://dummyjson.com/users")
    .then((res)=>res.json())
    .then((data)=>{
        setUser(data.users);
        setLoading(true)
        console.log(user);
    })
    .catch(error=>console.log(error));

    };
    if (!loading){
        return <div>Loading ....</div>
    }
    return (
        <div>
            {user.map((item)=>(
                <div>
                    <img src={item.image} alt="user-image"/>
                    <p>{item.firstName} {item.lastName} {item.maidenName}</p>
                    <h4>Details</h4>
                    <p>Age: {item.age}</p>
                    <p>Height: {item.height}</p>
                    <p>Gender: {item.gender}</p>
                    <p>Contact: {item.email}</p>




                </div>
            ))}

        </div>
    );

};
export default User;




