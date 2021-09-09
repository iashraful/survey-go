import { Layout, Menu } from "antd"
import { Link } from "react-router-dom";
import { UserOutlined } from '@ant-design/icons';
const { Header } = Layout;

const { SubMenu } = Menu

const TopNavbar = () => {
  return (
    <Layout>
      <Header style={{ position: 'fixed', zIndex: 1, width: '100%' }}>
        <div className="logo" />
        <Menu theme="dark" mode="horizontal" defaultSelectedKeys={[]}>
          <Menu.Item key="1">
            <Link to='/'>Home</Link>
          </Menu.Item>
          <Menu.Item key="3">nav 3</Menu.Item>

          <SubMenu key="sub1" icon={<UserOutlined/>} title="" style={{float: "right", marginLeft: 'auto'}}>
            <Menu.Item key="2">
              <Link to='/login'>Login</Link>
            </Menu.Item>
          </SubMenu>
        </Menu>
      </Header>
    </Layout>
  )
}

export default TopNavbar
