import React, { Component } from 'react';
import TaskBoard from '../components/task-board';
import '../css/slingshot-tasks.css';

class Tasks extends Component {
    state = {windowHeight:window.innerHeight,windowWidth:window.innerWidth,boards:{0:'todo',1:'inprogress',2:'inreview',3:'blocked',4:'completed'},boardtitles:['To Do','In Progress','In Review','Blocked','Completed'],colorcode:{0:'rgb(145,164,174)',1:'rgb(101,187,110)',2:'rgb(121,91,165)',3:'rgb(250,181,35)',4:'rgb(116,136,244)'}}
    componentDidMount()
    {
        window.addEventListener("resize", this.handleResize);
    }
    componentWillUnmount() {
        window.addEventListener("resize", this.handleResize);
       } 
    handleResize = (e) => {
        this.setState({windowHeight:window.innerHeight,windowWidth:window.innerWidth});
       };
    
    render() { 
        return ( 
            <div style={{backgroundColor:'#EDEFF5',position:'absolute',overflow:'scroll',left:60,top:60,width:this.state.windowWidth-60,height:this.state.windowHeight-60}}>
            <table>
            <span className="pagetitle">My Tasks<img src={require('../images/down-arrow.png')} alt=""/></span>
            <tr style={{marginTop:0}}>
            {this.state.boardtitles.map((board,idx) => <td style={{backgroundColor:'#EDEFF5'}}><TaskBoard bgc={this.state.colorcode[idx]} first={idx===0} tasks={this.props[this.state.boards[idx]]} title={board}/></td>)}
            </tr>
            </table>
            </div>
        );
    }
}
 
export default Tasks;