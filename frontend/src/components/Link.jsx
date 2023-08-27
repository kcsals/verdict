import useNavigation from '../hooks/use-navigation';

function Link({to, children}) {
 const {navigate} = useNavigation();

  const handleClick = (event) => {
    if(event.metaKey || event.ctrlKey){
      return;
    }
    event.preventDefault();

    navigate(to)
  };

  return (
    <a className="flex items-center text-white hover:text-red-600" href={to} onClick={handleClick}>{children}</a>
  )
}

export default Link