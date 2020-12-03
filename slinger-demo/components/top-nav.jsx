import React, { Component } from 'react';
import "../css/top-nav.css";

class NavBar extends Component {
    state = {}
    render() { 
        return ( 
            <nav className="navbar navbar-light box-shadow justify-content-between" style={{height:60}}>
                <a class="navbar-brand" href="#">
                <img src={require('../images/slingshotlogo.png')} alt=""/>
                <span className="group">Infragistics Adv Analytics<img src={require('../images/down-arrow.png')} alt=""/></span>
                </a>
                <form style={{marginRight:200,height:40}} class="form-inline">
                <div style={{width:300,padding:0}} className="input-group">
                <div class="input-group-prepend">
                <span class="input-group-text" id="basic-addon1" style={{backgroundColor:'transparent',borderRight:'none'}}><i style={{color:'black'}} class="fas fa-search"></i></span>
                </div>
                <input type="text" className="form-control" placeholder="Search..." aria-label="Username" aria-describedby="basic-addon1" style={{borderLeft:'none'}}>
                </input>
                </div>
                </form>
                <img style={{marginRight:-130}} src={require('../images/slingshot-notification.png')} alt=""/>
                <img style={{marginRight:-130}} src={require('../images/slingshot-chat.png')} alt=""/>
                <span className="profile">V</span>
            </nav>
        );
    }
}
 
export default NavBar;